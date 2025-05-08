"""
Just going to compute if it is even possible for a certain person to win it all
"""

from typing import Tuple, List, Dict, Literal
from copy import deepcopy
from random import choices as random_choice
from config import MATCHUP_ODDS, SIMULATION_TO_RUN
from my_types import Team, TEAMS_IN_ORDER, Matchup
from game import BRACKET_MATCHUP

PLAYER_CHOICES = {
    "Jack": (
        Team.THUNDER,
        Team.WARRIORS,
        Team.CLIPPERS,
        Team.PACERS,
    ),
    "Kunal": (
        Team.CELTICS,
        Team.CLIPPERS,
        Team.WARRIORS,
        Team.KNICKS,
    ),
    "Gabe": (
        Team.WARRIORS,
        Team.TIMBERWOLVES,
        Team.NUGGETS,
        Team.CELTICS,
    ),
    "Gavin": (
        Team.THUNDER,
        Team.CELTICS,
        Team.CAVALIERS,
        Team.WARRIORS,
    ),
    "Justin": (
        Team.CELTICS,
        Team.LAKERS,
        Team.WARRIORS,
        Team.NUGGETS,
    ),
    "Nick": (
        Team.THUNDER,
        Team.CELTICS,
        Team.LAKERS,
        Team.BUCKS,
    ),
    "Mike": (
        Team.LAKERS,
        Team.CLIPPERS,
        Team.WARRIORS,
        Team.CELTICS,
    ),
    "Mason": (
        Team.WARRIORS,
        Team.CLIPPERS,
        Team.BUCKS,
        Team.CELTICS,
    ),
    "Jay": (
        Team.LAKERS,
        Team.WARRIORS,
        Team.KNICKS,
        Team.CLIPPERS,
    ),
    "Sean": (
        Team.CLIPPERS,
        Team.WARRIORS,
        Team.HEAT,
        Team.GRIZZLIES,
    ),
    "Terminator": (
        Team.TIMBERWOLVES,
        Team.WARRIORS,
        Team.THUNDER,
        Team.CLIPPERS,
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
    Team.GRIZZLIES,
    Team.CLIPPERS,
    Team.LAKERS,
    Team.HEAT,
    Team.BUCKS,
    Team.PISTONS,
    Team.MAGIC,
    Team.ROCKETS,
    Team.WARRIORS,
]

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
    ties_amounts = 0


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

        # TODO: account for ties
        player_scores, wins_per_team = compute_all_scores_from_bracket(
            bracket=bracket_copy, player_choices=PLAYER_CHOICES
        )
        best_players = []
        best_score = 0
        for player, score in player_scores.items():
            if score > best_score:
                best_players = [player]
                best_score = score
            elif score == best_score:
                best_players.append(player)

        if len(best_players) > 1:
            ties_amounts += 1
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

        player_wins[best_player] += 1

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


    headers = ("Player", "Wins", "Percentage %")
    data = [
        (player, wins, f"{100*wins/SIMULATION_TO_RUN:.1f}")
        for player, wins in player_wins.items()
    ]
    # sort by number of wins in simulation
    data.sort(key=lambda x: x[1], reverse=1)
    print_tabulate(header=headers, data=data)
    print(
        f"encountered {ties_amounts:,} ties or {100 * ties_amounts/SIMULATION_TO_RUN:.1f}%"
    )

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


def team_choice():
    """Print how much each particular team is chosen"""
    header = ["Team", "# Chosen"]

    team_to_amount = {team: 0 for team in Team}
    for choices in PLAYER_CHOICES.values():
        for team in choices:
            team_to_amount[team] += 1

    data = [(team.name, amount) for team, amount in team_to_amount.items()]
    print("\n\nHow much was each team chosen by players")
    print_tabulate(header=header, data=data)


if __name__ == "__main__":
    sanity_checks()
    get_max_score_of_all_players()
    # player_similarity()
    # team_choice()
    simulate_random_brackets(method="geometric", aggregate_ranking=False, aggregate_vectors=False)
