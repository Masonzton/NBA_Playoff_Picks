"""
Just going to compute if it is even possible for a certain person to win it all
"""

from typing import Tuple, List, Dict, Literal
from copy import deepcopy, copy
from random import choices as random_choice
from config import MATCHUP_ODDS, SIMULATION_TO_RUN
from my_types import Team, TEAMS_IN_ORDER, Matchup
from game import BRACKET_MATCHUP
import itertools

PLAYER_CHOICES : dict[str, Tuple[Team, Team, Team, Team]]= {
    "Justin": (
        Team.THUNDER,
        Team.NUGGETS,
        Team.KNICKS,
        Team.ROCKETS,
    ),
    "Jack": (
        Team.MAGIC,
        Team.HAWKS,
        Team.THUNDER,
        Team.NUGGETS,
    ),
    "Kunal": (
        Team.THUNDER,
        Team.CAVALIERS,
        Team.TIMBERWOLVES,
        Team.HAWKS,
    ),
    "Nick": (
        Team.ROCKETS,
        Team.NUGGETS,
        Team.CAVALIERS,
        Team.THUNDER,
    ),
    "Gabe": (
        Team.THUNDER,
        Team.NUGGETS,
        Team.CELTICS,
        Team.CAVALIERS,
    ),
    "Mike": (
        Team.NUGGETS,
        Team.ROCKETS,
        Team.CELTICS,
        Team.PISTONS,
    ),
    "Mason": (
        Team.CAVALIERS,
        Team.HAWKS,
        Team.THUNDER,
        Team.NUGGETS,
    ),
    "Jay": (
        Team.NUGGETS,
        Team.KNICKS,
        Team.CAVALIERS,
        Team.ROCKETS,
    ),
    "Sean": (
        Team.SUNS,
        Team.TIMBERWOLVES,
        Team.LAKERS,
        Team.NUGGETS,
    ),
    "Gavin": (
        Team.THUNDER,
        Team.SPURS,
        Team.KNICKS,
        Team.CAVALIERS,
    ),
    "Terminator": (
        Team.ROCKETS,
        Team.NUGGETS,
        Team.CAVALIERS,
        Team.KNICKS,
    ),
}


def check_any_players_match():
    for playerA, choiceA in PLAYER_CHOICES.items():
        for playerB, choiceB in PLAYER_CHOICES.items():
            if playerA == playerB:
                continue

            if all([choice in choiceB for choice in choiceA]):
                print(f"{playerA} and {playerB} have the same choice of teams")


def print_tabulate(header: Tuple[str], data: List[Tuple]):
    """
    Print a list of information in a nice tabulated form
    """
    assert len(header) == len(data[0])
    # First, calculate the maximum width for each column
    col_widths = [
        max(len(str(row[i])) for row in data + [header]) for i in range(len(header))
    ]

    def print_list_to_markdown(data_row: list[str]):
        row_str = "| " + " | ".join(data_row) + " |"
        print(row_str)

    # Print the header
    header_str_list = [f"{header[i]:<{col_widths[i]}}" for i in range(len(header))]
    print_list_to_markdown(header_str_list)

    #print dash row
    dash_row = [ "-" * width for width in col_widths]
    print_list_to_markdown(dash_row)

    # Print each row
    for row in data:
        assert len(row) == len(header)
        row_str_list = [f"{row[i]:<{col_widths[i]}}" for i in range(len(row))]
        print_list_to_markdown(row_str_list)


def greedy_fill_bracket(bracket: Matchup, choices: Tuple[Team, Team, Team, Team]):
    if bracket.get_team() is not None:
        # nothing to fill out since the bracket has it's winners already
        return
    elif type(bracket.teamA) == Matchup:
        # fill out the left and right bracket's first if they are a matchup object
        if bracket.teamA.get_team() is None:
            greedy_fill_bracket(bracket=bracket.teamA, choices=choices)
        if bracket.teamB.get_team() is None:
            greedy_fill_bracket(bracket=bracket.teamB, choices=choices)
    else:
        # this is an unfilled out team thing
        assert type(bracket.teamB) == Team
        assert type(bracket.teamA) == Team

    # let's make a choice here. Both team a and b should be decided now
    teamA = bracket.teamA.get_team()
    teamB = bracket.teamB.get_team()
    assert teamA is not None
    assert teamB is not None
    scoreA = teamA.points if teamA in choices else 0
    scoreB = teamB.points if teamB in choices else 0

    assert bracket.winsA < 4
    assert bracket.winsB < 4

    if scoreA == 0 and scoreB == 0:
        # doesn't matter who wins really. Just want less games in general
        # and also the better team to win so less points to other people

        # least new points generated
        if teamA.points < teamB.points:
            bracket.winsA = 4
        elif teamB.points < teamA.points:
            bracket.winsB = 4
        # less games option
        elif bracket.winsA > bracket.winsB:
            bracket.winsA = 4
        else:
            bracket.winsB = 4
    elif scoreA == 0 and scoreB > 0:
        # we want B to win it all
        bracket.winsB = 4
    elif scoreB == 0 and scoreA > 0:
        # we want A to win it all
        bracket.winsA = 4
    elif scoreA > 0 and scoreB > 0:
        # we want a really close game
        if scoreA > scoreB:
            bracket.winsA = 4
            bracket.winsB = 3
        else:
            bracket.winsB = 4
            bracket.winsA = 3


def gather_wins_per_team(bracket: Matchup) -> Dict[Team, int]:
    # search the tree and accumulates wins for team
    # bfs
    queue: List[Matchup] = []
    queue.append(bracket)

    wins_for_each_team = {team: 0 for team in Team}

    while queue:
        m = queue.pop(0)

        # act on m
        teamA = m.teamA.get_team()
        if teamA is not None:
            wins_for_each_team[teamA] += m.winsA
        teamB = m.teamB.get_team()
        if teamB is not None:
            wins_for_each_team[teamB] += m.winsB

        # add more matchup's to the queue
        if type(m.teamA) == Matchup:
            queue.append(m.teamA)
            queue.append(m.teamB)

    return wins_for_each_team


def compute_individual_score_from_bracket(
    bracket: Matchup, choices: Tuple[Team, Team, Team, Team]
) -> int:
    wins_for_each_team = gather_wins_per_team(bracket=bracket)
    points = 0
    for choice in choices:
        points += wins_for_each_team[choice] * choice.points

    # DEBUG
    # headers = ("Team", "Wins", "Points")
    # data = [ (team.name, wins_for_each_team[team], wins_for_each_team[team] * team.points) for team in choices]
    # print_tabulate(header=headers, data=data)

    return points


def compute_all_scores_from_bracket(
    bracket: Matchup, player_choices: Dict[str, Tuple[Team, Team, Team, Team]]
) -> Tuple[Dict[str, int], Dict[Team, int]]:
    """Return scores dict plus wins per team dictionary"""
    wins_for_each_team = gather_wins_per_team(bracket=bracket)
    ret = {}
    for player, choices in player_choices.items():
        points = sum([(wins_for_each_team[team] * team.points) for team in choices])
        ret[player] = points

    return ret, wins_for_each_team


def get_max_score_of_all_players():
    print(
        "* means they can win in their best case scenario, _ means they don't happen to win in "
        "the scenario created. Not exhaustive"
    )
    data = []
    for player, choices in PLAYER_CHOICES.items():
        ideal_bracket = deepcopy(BRACKET_MATCHUP)
        # depth first recursively fill out the bracket in a greedy way
        greedy_fill_bracket(ideal_bracket, choices)
        best_score = compute_individual_score_from_bracket(
            bracket=ideal_bracket, choices=choices
        )

        best_opponent_player = None
        best_opponent_score = 0
        for playerO, choiceO in PLAYER_CHOICES.items():
            if playerO == player:
                continue
            scoreO = compute_individual_score_from_bracket(
                bracket=ideal_bracket, choices=choiceO
            )
            if scoreO > best_opponent_score:
                best_opponent_score = scoreO
                best_opponent_player = playerO

        current_score = compute_individual_score_from_bracket(
            bracket=BRACKET_MATCHUP, choices=choices
        )
        if best_score > best_opponent_score:
            winning = "*"
        else:
            winning = "_"
        data.append(
            (
                player,
                winning,
                current_score,
                best_score,
                # best_opponent_player,
                # best_opponent_score,
            )
        )

    # sort by current score
    data.sort(key=lambda x: x[2], reverse=True)
    print_tabulate(
        header=(
            "player",
            "W",
            "Current Score",
            "Max Score",
            # "Best Opponent",
            # "Best Opponent Score",
        ),
        data=data,
    )


def random_uniform_bracket_fill(bracket: Matchup):
    if bracket.get_team() is not None:
        # nothing to fill out since the bracket has it's winners already
        return
    elif type(bracket.teamA) == Matchup:
        # fill out the left and right bracket's first if they are a matchup object
        if bracket.teamA.get_team() is None:
            random_uniform_bracket_fill(bracket=bracket.teamA)
        if bracket.teamB.get_team() is None:
            random_uniform_bracket_fill(bracket=bracket.teamB)
    else:
        # this is an unfilled out team thing
        assert type(bracket.teamB) == Team
        assert type(bracket.teamA) == Team

    # randomly assign the wins for this matchup
    # Note this is a uniform selection, this is not meant to be realistic but rather maximum exploration
    a_win_options = [(4, b) for b in range(bracket.winsB, 4)]  # b can win up to 3 times
    b_win_options = [(a, 4) for a in range(bracket.winsA, 4)]  # a can win up to 3 times
    options = a_win_options + b_win_options
    outcome = random_choice(population=options)
    bracket.winsA, bracket.winsB = outcome[0]


def random_geometric_bracket_fill(bracket: Matchup):
    if bracket.get_team() is not None:
        # nothing to fill out since the bracket has it's winners already
        return
    elif type(bracket.teamA) == Matchup:
        # fill out the left and right bracket's first if they are a matchup object
        if bracket.teamA.get_team() is None:
            random_geometric_bracket_fill(bracket=bracket.teamA)
        if bracket.teamB.get_team() is None:
            random_geometric_bracket_fill(bracket=bracket.teamB)
    else:
        # this is an unfilled out team thing
        assert type(bracket.teamB) == Team
        assert type(bracket.teamA) == Team

    # keep on adding random wins until one team has won the matchup
    # probabilities are determined from MATCHUP_ODDS array
    while bracket.get_team() is None:
        bracket.add_random_win()

ELIMINATED_TEAMS = [
]

def set_wins_by_match_id(root: Matchup, id: List[int], winsA: int, winsB: int):
    id_list = copy(id)
    matchup = root
    while id_list:
        if id_list[0] == 0:
            matchup = matchup.teamA
        elif id_list[0] == 1:
            matchup = matchup.teamB
        else:
            raise ValueError(f"unexpected value {id_list[0]}")
        id_list.pop(0)
    
    assert winsA >= matchup.winsA
    assert winsB >= matchup.winsB
    assert (winsA == 4) or (winsB == 4)
    assert matchup.get_team() is None
    matchup.winsA = winsA
    matchup.winsB = winsB

def get_possibility_list_from_matchup(matchup: Matchup) -> List[Tuple[int, int]]:
    # A wins
    a_win_options = [(4, b) for b in range(matchup.winsB, 4)]  # b can win up to 3 times
    b_win_options = [(a, 4) for a in range(matchup.winsA, 4)]  # a can win up to 3 times
    return a_win_options + b_win_options

def get_best_player(player_scores, wins_per_team):
    best_players = []
    best_score = 0
    for player, score in player_scores.items():
        if score > best_score:
            best_players = [player]
            best_score = score
        elif score == best_score:
            best_players.append(player)

    if len(best_players) > 1:
        # see if their first choice team has scored more points than theirs
        for idx in range(4):
            best_sub_score = 0
            best_sub_players = []
            for player in best_players:
                choice = PLAYER_CHOICES[player]
                team = choice[idx]
                sub_score = team.points * wins_per_team[team]
                if sub_score > best_sub_score:
                    best_sub_players = [player]
                    best_score = sub_score
                elif sub_score == best_sub_score:
                    best_sub_players.append(player)
            if len(best_sub_players) > 1:
                best_players = best_sub_players
            else:
                best_player = best_sub_players[0]
                break
        else:
            assert False, "should have found a best player in the tie scenario"
    else:
        best_player = best_players[0]
    
    return best_player

def play_all_scenarios():
    """
    Enumerate all possibilities
    """

    to_visit: List[Tuple[List[int], Matchup]] = [([], BRACKET_MATCHUP)]

    game_list: List[Tuple[List[int], List[Tuple[int, int]]]] = []

    while to_visit:
        node_id, node = to_visit.pop(0)
        # process node
        if node.get_team() is None:
            # add to the games_list
            game_list.append((node_id, get_possibility_list_from_matchup(node)))

            # add more nodes to visit
            to_visit.append((node_id + [0], node.teamA))
            to_visit.append((node_id + [1], node.teamB))

    game_comb : List[List[Tuple[int, int]]] = [t[1] for t in game_list]
    total_outcomes = 0

    wins_per_player = {player: 0 for player in PLAYER_CHOICES.keys()}
    for all_outcomes in itertools.product(*game_comb):
        bracket_copy = deepcopy(BRACKET_MATCHUP)
        for idx, game_outcome in enumerate(all_outcomes):
            game_id = game_list[idx][0]
            set_wins_by_match_id(bracket_copy, game_id, game_outcome[0], game_outcome[1])
        assert bracket_copy.get_team() is not None

        player_scores, wins_per_team = compute_all_scores_from_bracket(
            bracket=bracket_copy, player_choices=PLAYER_CHOICES
        )
        best_player = get_best_player(
            player_scores=player_scores,
            wins_per_team=wins_per_team
        )
        wins_per_player[best_player] += 1
        total_outcomes += 1


    print(f"{total_outcomes:,} possible brackets left")

    headers = ("Player", "Wins", "Percentage %")
    data = [
        (player, wins, f"{100*wins/total_outcomes:.1f}")
        for player, wins in wins_per_player.items()
    ]
    # sort by number of wins in simulation
    data.sort(key=lambda x: x[1], reverse=1)
    print_tabulate(header=headers, data=data)


# Constructing all possible brackets is impossible when there are 15 games to play
# and 8 different variations of point breakdown between the team. Or in other words
# 8^15 or 10 trillion
def simulate_random_brackets(
    method: Literal["uniform", "geometric"],
    aggregate_ranking: bool = False,
    aggregate_vectors: bool = False
):
    """
    Simulate different bracket combinations. Geometric will use the odds prescribed in the
    MATCHUP_ODDS which is useful for realistic odds, uniform will just choose a random outcome for
    every series, which is useful for trying more options / trying to find the outcome that secures a win
    for a player.

    Args:
        aggregate_ranking: collect metrics on distribution of rankings and matchup between players
    """
    print("\n \n")
    print(
        f"******Running {SIMULATION_TO_RUN:,} random simulations using {method} method*****"
    )
    player_wins = {player: 0 for player in PLAYER_CHOICES.keys()}
    player_total_score = {player: 0 for player in PLAYER_CHOICES.keys()}


    if aggregate_ranking:
        player_list = list(PLAYER_CHOICES.keys())
        wins_against_other_players = {player1: {player2: 0 for player2 in player_list} for player1 in player_list}
        player_ranking_distribution = {player: [0 for _ in player_list]  for player in player_list}
    
    if aggregate_vectors:
        MAX_TEAM_WINS = 10_000 # nonsense high number
        MIN_TEAM_WINS = 0
        player_vectors_min = {player: [MAX_TEAM_WINS for _ in Team] for player in PLAYER_CHOICES.keys()}
        player_vectors_max = {player: [MIN_TEAM_WINS for _ in Team] for player in PLAYER_CHOICES.keys()}

    for _ in range(SIMULATION_TO_RUN):
        bracket_copy = deepcopy(BRACKET_MATCHUP)
        if method == "uniform":
            random_uniform_bracket_fill(bracket_copy)
        elif method == "geometric":
            random_geometric_bracket_fill(bracket_copy)
        else:
            raise NotImplementedError(f"{method} not implemented")

        player_scores, wins_per_team = compute_all_scores_from_bracket(
            bracket=bracket_copy, player_choices=PLAYER_CHOICES
        )

        best_player = get_best_player(player_scores=player_scores, wins_per_team=wins_per_team)

        player_wins[best_player] += 1
        for player in PLAYER_CHOICES.keys():
            player_total_score[player] += player_scores[player]

        if aggregate_vectors:
            wins_per_team_vector = [wins_per_team[team] for team in Team]
            # for the best player, take mins and maxes across the vector
            for index, _ in enumerate(Team):
                player_vectors_max[best_player][index] = max(player_vectors_max[best_player][index], wins_per_team_vector[index])
                player_vectors_min[best_player][index] = min(player_vectors_min[best_player][index], wins_per_team_vector[index])
        
        if aggregate_ranking:
            for player_one in player_list:
                for player_two in player_list:
                    if player_scores[player_one] > player_scores[player_two]:
                        wins_against_other_players[player_one][player_two] += 1
            player_scores_list = [(player, score) for player, score in player_scores.items()]
            player_scores_list.sort(key=lambda x: x[1], reverse=True)
            assert player_scores_list[0][1] >= player_scores_list[1][1]
            for idx, value in enumerate(player_scores_list):
                player, _ = value
                player_ranking_distribution[player][idx] += 1


    headers = ("Player", "Wins", "Percentage %", "Average Score")
    data = [
        (player, wins, f"{100*wins/SIMULATION_TO_RUN:.1f}", (player_total_score[player] / SIMULATION_TO_RUN))
        for player, wins in player_wins.items()
    ]
    # sort by number of wins in simulation
    data.sort(key=lambda x: x[1], reverse=1)
    print_tabulate(header=headers, data=data)

    if aggregate_ranking:
        print("\n\nWhat % of times each player wins against another player, useful for seeing which player 'knocked out' each other")
        header_ag = ["Player"] + player_list
        data = [ [player1] + [f"{100*wins_against_other_players[player1][player2]/SIMULATION_TO_RUN:.1f}" for player2 in player_list] for player1 in player_list]
        print_tabulate(header_ag, data)

        print("\n\nDistribution of ranking for each player")
        header = ["Player"] + [i+1 for i in range(len(player_list))]
        data = [ [player] + [f"{100*player_ranking_distribution[player][idx]/SIMULATION_TO_RUN:.1f}" for idx in range(len(player_list))] for player in player_list]
        print_tabulate(header, data)
    
    if aggregate_vectors:
        for player in PLAYER_CHOICES.keys():
            print(player)
            for idx, team in enumerate(Team):
                if team in ELIMINATED_TEAMS:
                    continue
                print(f"{team}: min: {player_vectors_min[player][idx]} max: {player_vectors_max[player][idx]}")
        # print(f"max: {player_vectors_max}")
        # print(f"min: {player_vectors_min}")
    
    return data


def sanity_checks():
    check_any_players_match()

    if SIMULATION_TO_RUN > 10_000:
        time_to_run = int((SIMULATION_TO_RUN / 10_000) * 2)
        print(
            f"WARNING: Doing {SIMULATION_TO_RUN} simulations will take at least {time_to_run} seconds. Consider using a smaller number of runs"
        )

    for idx, row in enumerate(MATCHUP_ODDS):
        # order of those matchup rows can not be changed
        assert row[0] == TEAMS_IN_ORDER[idx].team_name, "MATCHUP_ODDS rows were re-arranged, that's not allowed since it's fragile..."

    # TODO: Check that the BRACKET_MATCHUP doesn't contain any duplicate teams and does not skip a team


def player_similarity():
    """Print how many teams in common each player has"""
    print("\n\nHow many teams each player has in common")
    header = list(PLAYER_CHOICES.keys())

    data = []
    for player in header:
        choices = set(PLAYER_CHOICES[player])
        row = [player]
        for other_player in header:
            other_choices = set(PLAYER_CHOICES[other_player])
            row.append(len(other_choices & choices))
        data.append(row)

    print_tabulate(header=["Player"] + header, data=data)

    data_matches : list[Tuple[str, int, str]]= []
    print("\n\nEach players most common matching's")
    for idx, player in enumerate(header):
        row = data[idx]
        matches : list[int] = row[1:]
        assert row[0] == player

        matches_minus_player = deepcopy(matches)
        matches_minus_player.pop(idx)
        max_val = max(matches_minus_player)

        all_max_indices = [i for i, x in enumerate(matches) if x == max_val]

        matching_players = [header[i] for i in all_max_indices]
        data_matches.append((player, max_val, str(matching_players)))
    
    header = ("Player", "Most Matches", "Matching Players")
    data_matches.sort(key= lambda x: x[1], reverse=True)
    print_tabulate(header, data_matches)




def team_choice():
    """Print how much each particular team is chosen"""
    header = ["Team", "# Chosen"]

    team_to_amount = {team: 0 for team in Team}
    for choices in PLAYER_CHOICES.values():
        for team in choices:
            team_to_amount[team] += 1

    data = [(team.name, amount) for team, amount in team_to_amount.items()]
    data.sort(key=lambda x: x[1], reverse=True)
    print("\n\nHow much was each team chosen by players")
    print_tabulate(header=header, data=data)
    #TODO: sort by most common to least common

def get_best_possible_bracket():
    """Based on the probabilities set up in MATCHUP_ODDS, simulate to get the bracket with the best possible score"""

    # TODONE fill out player choice will all 4 team choices
    all_player_choices : list[Tuple[Team, Team, Team, Team]]= list(itertools.combinations(Team, 4))

    global PLAYER_CHOICES
    PLAYER_CHOICES = {str(i) : all_player_choices[i] for i in range(len(all_player_choices))}

    # for each combination, simulate a random bracket, and then record the score
    # might be better to actually fill out a player_choice with every single possible combination, run all brackets
    # and 1, see who comes out on top, and 2. see which one has the highest average score
    headers, data = simulate_random_brackets(method="geometric", aggregate_ranking=False, aggregate_vectors=False)

    print_tabulate(header=headers, data=data[0:10])
    # TODONE: modify function to return table + average score of each player
    # TODONE: Print out team that has the highest win % and the team with highest average score
    # TODO: fill out matchup odds based on BPI



if __name__ == "__main__":
    sanity_checks()
    # get_best_possible_bracket()
    get_max_score_of_all_players()
    player_similarity()
    team_choice()
    simulate_random_brackets(method="geometric", aggregate_ranking=True, aggregate_vectors=False)
    # TODO: in aggregate_vectors, should only print people that have a chance of winning
    # Should print min scores of each team that person has, and max scores of each team that person doesn't have
    # play_all_scenarios()
