"""
A file for computing the matchup odds between different NBA teams based on ESPN's published odds and BPI ranking

https://www.espn.com/nba/bpi/_/view/playoffs
"""

import requests
from my_types import Team
from game import Matchup, BRACKET_MATCHUP
from config import MATCHUP_ODDS
from typing import Optional, Any, Tuple, List, Union
import json
import numpy as np

POWER_INDEX_URL = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2026/powerindex?lang=en&region=us&limit=100&page=1"
POWER_INDEX_DATA_JSON = "power_index_data.json"

TEAM_POWER_DATA : dict[str, dict[str, float]]= {}

def print_tabulate(header: Tuple[str,...], data: List[Tuple[Any,...]]):
    """
    Print a list of information in a nice tabulated form
    """
    assert len(header) == len(data[0])
    # First, calculate the maximum width for each column
    col_widths = [
        max(len(str(row[i])) for row in data + [header]) for i in range(len(header))
    ]

    # Print the header
    header_str_list = [f"{header[i]:<{col_widths[i]}}" for i in range(len(header))]
    header_str = "  ".join(header_str_list)
    print(header_str)
    print("-" * (sum(col_widths) + 6))

    # Print each row
    for row in data:
        assert len(row) == len(header)
        row_str_list = [f"{row[i]:<{col_widths[i]}}" for i in range(len(row))]
        row_str = "  ".join(row_str_list)
        print(row_str)

def convert_team_name_to_standard(name: str) -> str:
    name = name.lower()
    name = name.replace(" ", "_")
    if name == "76ers":
        name = "SEVENTY_SIXERS"
    return name

def get_odds_for_each_team():
    print("getting odds for each team")
    # First we need to grab the power indexes
    power_index_result = requests.get(POWER_INDEX_URL)
    power_index_result.raise_for_status()

    power_index_dict = power_index_result.json()

    data_to_grab = ["bpi", "probmakeplayoffs", "probmakeconfsemi", "probmakeconfchamp", "probmaketitlegame", "probwintitle"]
    headers = ["Team Name", "Season type"] + data_to_grab

    data : list[Tuple[Any]]= []

    for team_entry in power_index_dict["items"]:

        # TODO: wrap in try except block to avoid blowing up cause one team messed up

        if team_entry["seasonType"] != 3:
            continue

        # try: 
        team_ref_url = team_entry["team"]["$ref"]
        team_ref_result = requests.get(team_ref_url)
        team_ref_result.raise_for_status()
        team_ref_data = team_ref_result.json()
        team_name : str = convert_team_name_to_standard(team_ref_data["name"])


        name_to_stats : dict[str, float] = dict()
        for stat_entry in team_entry["stats"]:
            if "name" in stat_entry and "value" in stat_entry:
                name_to_stats[stat_entry["name"]] = stat_entry["value"]

        display_entry : list [Any]= [team_name, team_entry["seasonType"]]
        for header_field in data_to_grab:
            if header_field in name_to_stats:
                display_entry.append(name_to_stats[header_field])
            else:
                display_entry.append(None)
        data.append(tuple(display_entry))
    
    print_tabulate(header=tuple(headers), data=data)

    data_json = {row[0] : {header: row[idx] for idx, header in enumerate(headers)}  for row in data}
    with open(POWER_INDEX_DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(data_json, f)

def get_attribute(team: Team, attribute: str) -> float:
    return TEAM_POWER_DATA[team.team_name.lower()][attribute] / 100.0

def get_possible_teams(node: Union[Matchup, Team]) -> List[Team]:
    """
    Recursively collect all possible teams that could emerge from this node.
    If node is a Team, return [node].
    If node is a Matchup with a resolved winner, return [winner].
    Otherwise return all teams from both sides.
    """
    if isinstance(node, Team):
        return [node]
    # node is a Matchup
    winner = node.get_team()
    if winner is not None:
        return [winner]
    return get_possible_teams(node.teamA) + get_possible_teams(node.teamB)


def get_tree_depth(node: Union[Matchup, Team]) -> int:
    """
    Returns the depth of the subtree rooted at node.
    A leaf Matchup (both children are Teams) has depth 0.
    """
    if isinstance(node, Team):
        return -1  # not a matchup node
    if isinstance(node.teamA, Team) and isinstance(node.teamB, Team):
        return 0
    depth_a = get_tree_depth(node.teamA) if isinstance(node.teamA, Matchup) else -1
    depth_b = get_tree_depth(node.teamB) if isinstance(node.teamB, Matchup) else -1
    return max(depth_a, depth_b) + 1


# Map from tree depth (order) to the ESPN BPI attribute representing
# "probability of winning this round" (i.e. making it to the next round).
# order 0 = first round  → winner makes conference semis
# order 1 = conf semis   → winner makes conf finals
# order 2 = conf finals  → winner makes NBA Finals
# order 3 = NBA Finals   → winner wins title
ORDER_TO_ATTRIBUTE = {
    0: "probmakeconfsemi",
    1: "probmakeconfchamp",
    2: "probmaketitlegame",
    3: "probwintitle",
}


def get_prob_reaching_round(team: Team, order: int) -> float:
    """
    Probability that `team` reaches the round represented by `order`.
    order=0 means the first-round matchup itself, so every playoff team
    has probability 1.0 of reaching it.
    For higher orders we use the ESPN BPI attribute of the *previous* round.
    """
    if order == 0:
        return 1.0
    attr = ORDER_TO_ATTRIBUTE[order - 1]
    return get_attribute(team, attr)


def compute_odds_sub(bracket: Matchup, order: int = None):
    """
    Recursively compute per-matchup win probabilities from ESPN BPI data.

    Parameters
    ----------
    bracket : Matchup
        The current node in the bracket tree.
    order : int
        Depth of this node from the leaves (leaves = 0).
        Computed automatically on the first call.
    """
    # Resolve order from tree structure if not provided
    if order is None:
        order = get_tree_depth(bracket)

    # Base case: bracket already has a resolved winner – nothing to do
    if bracket.get_team() is not None:
        return

    # Recurse into children first so deeper nodes are solved before parents
    if isinstance(bracket.teamA, Matchup) and bracket.teamA.get_team() is None:
        compute_odds_sub(bracket.teamA, order - 1)
    if isinstance(bracket.teamB, Matchup) and bracket.teamB.get_team() is None:
        compute_odds_sub(bracket.teamB, order - 1)

    # Gather all possible teams from each side
    list_A: List[Team] = get_possible_teams(bracket.teamA)
    list_B: List[Team] = get_possible_teams(bracket.teamB)

    n_A = len(list_A)
    n_B = len(list_B)
    n_unknowns = n_A * n_B          # x[i,j] = P(list_A[i] beats list_B[j])
    n_equations = n_A + n_B

    # Under-constrained: skip this node
    if n_equations < n_unknowns:
        print(
            f"[SKIP] order={order}  |A|={n_A}  |B|={n_B}  "
            f"equations={n_equations} < unknowns={n_unknowns}"
        )
        return

    # ------------------------------------------------------------------ #
    # Build the linear system  A_mat @ x_vec = c_vec
    #
    # Unknowns are laid out row-major: x[i*n_B + j] = P(A_i beats B_j)
    #
    # Equation group 1 (rows 0 .. n_A-1):  for each team A_i
    #   sum_j [ P(B_j reaches this round) * x[i,j] ] = P(A_i advances)
    #
    # Equation group 2 (rows n_A .. n_A+n_B-1):  for each team B_j
    #   sum_i [ P(A_i reaches this round) * (1 - x[i,j]) ] = P(B_j advances)
    # ------------------------------------------------------------------ #

    A_mat = np.zeros((n_equations, n_unknowns))
    c_vec = np.zeros(n_equations)

    # --- Group 1: advancement equations for each team in list_A ---
    for i, team_a in enumerate(list_A):
        prob_a_advances = get_attribute(team_a, ORDER_TO_ATTRIBUTE[order])
        print(f"{team_a} : {prob_a_advances}")
        c_vec[i] = prob_a_advances
        for j, team_b in enumerate(list_B):
            prob_b_reaches = get_prob_reaching_round(team_b, order)
            col = i * n_B + j
            A_mat[i, col] = prob_b_reaches

    # --- Group 2: advancement equations for each team in list_B ---
    for j, team_b in enumerate(list_B):
        row = n_A + j
        prob_b_advances = get_attribute(team_b, ORDER_TO_ATTRIBUTE[order])
        print(f"{team_b} : {prob_b_advances}")
        c_vec[row] = prob_b_advances
        for i, team_a in enumerate(list_A):
            prob_a_reaches = get_prob_reaching_round(team_a, order)
            col = i * n_B + j
            # coefficient of x[i,j] is  -prob_a_reaches  (from the (1-x) expansion)
            A_mat[row, col] = -prob_a_reaches
            # constant shift: sum_i P(A_i reaches) * 1  moves to RHS
            c_vec[row] += prob_a_reaches  # c = P(B_j advances) + ... wait, see below

    # Re-derive group-2 RHS cleanly:
    # sum_i P(A_i reaches) * (1-x[i,j]) = P(B_j advances)
    # => -sum_i P(A_i reaches)*x[i,j] = P(B_j advances) - sum_i P(A_i reaches)
    for j, team_b in enumerate(list_B):
        row = n_A + j
        prob_b_advances = get_attribute(team_b, ORDER_TO_ATTRIBUTE[order])
        total_prob_a_reaches = sum(get_prob_reaching_round(a, order) for a in list_A)
        c_vec[row] = prob_b_advances - total_prob_a_reaches

    print(f"A_mat: {A_mat}, c_vec: {c_vec}")
    # Solve via least-squares (handles over-determined or exactly-determined systems)
    x_vec, residuals, rank, sv = np.linalg.lstsq(A_mat, c_vec, rcond=None)

    # Clip solutions to [0, 1] – numerical noise can push slightly outside
    x_vec = np.clip(x_vec, 0.0, 1.0)

    # ------------------------------------------------------------------ #
    # Print results
    # ------------------------------------------------------------------ #
    print(f"\n{'='*60}")
    print(f"Matchup odds  (order={order}, {n_A} vs {n_B} possible teams)")
    print(f"{'='*60}")

    name_width = max(len(t.team_name) for t in list_A + list_B)
    header = " " * (name_width + 2) + "  ".join(
        f"{t.team_name:>{name_width}}" for t in list_B
    )
    print(header)
    print("-" * len(header))

    for i, team_a in enumerate(list_A):
        row_vals = []
        for j in range(n_B):
            prob = x_vec[i * n_B + j]
            row_vals.append(f"{prob:>{name_width}.3f}")
        print(f"{team_a.team_name:<{name_width}}  " + "  ".join(row_vals))

    print()


def compute_odds():
    print("Computing odds for each matchup")
    global TEAM_POWER_DATA
    with open(POWER_INDEX_DATA_JSON, 'r') as file:
        TEAM_POWER_DATA = json.load(file)

    # go down to the lowest level of the tree
    assert type(BRACKET_MATCHUP.teamA) == Matchup
    compute_odds_sub(BRACKET_MATCHUP.teamA)



def main():
    # get_odds_for_each_team()
    compute_odds()
    pass

if __name__ == "__main__":
    main()