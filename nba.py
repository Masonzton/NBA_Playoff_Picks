"""
Just going to compute if it is even possible for a certain person to win it all
"""

from enum import Enum
from typing import Union, Tuple, List, Dict, Literal
from copy import deepcopy
from functools import cached_property
from random import choices as random_choice


class Team(Enum):
    THUNDER = ("THUNDER", 1)
    GRIZZLIES = ("GRIZZLIES", 8)
    NUGGETS = ("NUGGETS", 4)
    CLIPPERS = ("CLIPPERS", 5)
    LAKERS = ("LAKERS", 3)
    TIMBERWOLVES = ("TIMBERWOLVES", 6)
    ROCKETS = ("ROCKETS", 2)
    WARRIORS = ("WARRIORS", 7)
    CAVALIERS = ("CAVALIERS", 1)
    HEAT = ("HEAT", 8)
    PACERS = ("PACERS", 4)
    BUCKS = ("BUCKS", 5)
    KNICKS = ("KNICKS", 3)
    PISTONS = ("PISTONS", 6)
    CELTICS = ("CELTICS", 2)
    MAGIC = ("MAGIC", 7)

    def __init__(self, name: str, position: int):
        self.team_name = name
        self.position = position

    @cached_property
    def points(self) -> int:
        if self.position <= 2:
            return 1
        elif self.position <= 4:
            return 2
        elif self.position <= 6:
            return 3
        elif self.position <= 8:
            return 4

    def get_team(self) -> "Team":
        return self

# Matchup odds between each two possible teams that can play together
# -1 are filled out automatically based on reciprocal odds or are teams playing themselves
# probability indicates odds that teamA on the left will beat teamB above. For example, Thunder have a 75% chance of beating grizzlies each game
MATCHUP_ODDS = (
 # (                THUNDER GRIZZLIES NUGGETS CLIPPERS LAKERS TIMBERWOLVES ROCKETS WARRIORS CAVALIERS HEAT PACERS BUCKS KNICKS PISTONS CELTICS MAGIC
(Team.THUNDER,      -1,     0.75,     0.5,    0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.GRIZZLIES,    -1,     -1,       0.5,    0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.NUGGETS,      -1,     -1,       -1,     0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.CLIPPERS,     -1,     -1,       -1,     -1,      0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.LAKERS,       -1,     -1,       -1,     -1,      -1,    0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.TIMBERWOLVES, -1,     -1,       -1,     -1,      -1,    -1,          0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.ROCKETS,      -1,     -1,       -1,     -1,      -1,    -1,          -1,     0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.WARRIORS,     -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.CAVALIERS,    -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.HEAT,         -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.PACERS,       -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    0.5,  0.5,   0.5,    0.5,    0.5,),
(Team.BUCKS,        -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   0.5,   0.5,    0.5,    0.5,),
(Team.KNICKS,       -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    0.5,    0.5,    0.5,),
(Team.PISTONS,      -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     0.5,    0.5,),
(Team.CELTICS,      -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     -1,     0.5,),
(Team.MAGIC,        -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     -1,     -1, ),
)

TEAMS_IN_ORDER = [
    Team.THUNDER,
    Team.GRIZZLIES,
    Team.NUGGETS,
    Team.CLIPPERS,
    Team.LAKERS,
    Team.TIMBERWOLVES,
    Team.ROCKETS,
    Team.WARRIORS,
    Team.CAVALIERS,
    Team.HEAT,
    Team.PACERS,
    Team.BUCKS,
    Team.KNICKS,
    Team.PISTONS,
    Team.CELTICS,
    Team.MAGIC,
]

TEAM_TO_INDEX = {team: idx for idx, team in enumerate(TEAMS_IN_ORDER)}

def get_matchup_odds(teamA: Team, teamB: Team):
    """
    Get odds that teamA beats teamB
    """
    # note that we need to add 1 when accessing the second index due to the first entry being an enum
    idxA = TEAM_TO_INDEX[teamA]
    idxB = TEAM_TO_INDEX[teamB]
    prob = MATCHUP_ODDS[idxA][idxB+1]
    # if this is a negative one, then use the other side of the table 
    if prob == -1:
        prob = 1.0 - MATCHUP_ODDS[idxB][idxA+1]
    
    # probabilities should always be between 0 and 1
    if not (prob >= 0.0 and prob <= 1.0):
        breakpoint() 
    assert prob >= 0.0
    assert prob <= 1.0
    return prob

class Matchup:
    def __init__(
        self,
        teamA: Union[Team, "Matchup"],
        teamB: Union[Team, "Matchup"],
        winsA: int,
        winsB: int,
    ):
        self.teamA = teamA
        self.teamB = teamB
        self.winsA = winsA
        self.winsB = winsB

        # declare winner if a team has gotten 4 wins
        if winsA == 4:
            self._winner = teamA.get_team()
        elif winsB == 4:
            self._winner = teamB.get_team()
        else:
            self._winner = None

        # update child matchup to point up. Idk why
        self.parent = None
        if type(teamA) == Matchup:
            self.teamA.parent = self
        if type(teamB) == Matchup:
            self.teamB.parent = self

    def get_team(self) -> "Team":
        """Updates winner and returns winner"""
        if self.winsA == 4:
            self._winner = self.teamA.get_team()
        elif self.winsB == 4:
            self._winner = self.teamB.get_team()
        return self._winner
    
    def add_random_win(self):
        # get the team from the matchup odds
        teamA = self.teamA.get_team()
        teamB = self.teamB.get_team()
        # should never be calling this function if either side of the matchup is not determined
        assert teamA is not None
        assert teamB is not None
        probability_A_win = get_matchup_odds(teamA=teamA, teamB=teamB)
        
        team = random_choice(population=['a', 'b'], weights=[probability_A_win, (1- probability_A_win)])[0]
        if team == 'a':
            self.winsA += 1
        elif team == 'b':
            self.winsB += 1
        else:
            raise ValueError(f"Unexpected random choice {team}")

# bracket breakdown
BRACKET_MATCHUP = Matchup(
    # west
    winsA=0,
    teamA=Matchup(
        winsA=0, #Thunder
        teamA=Matchup(
            # 1,8
            winsA=0,
            teamA=Matchup(
                winsA=4,
                teamA=Team.THUNDER,
                winsB=0,
                teamB=Team.GRIZZLIES,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=2,
                teamA=Team.NUGGETS,
                winsB=2,
                teamB=Team.CLIPPERS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=0,
            teamA=Matchup(
                winsA=1,
                teamA=Team.LAKERS,
                winsB=3,
                teamB=Team.TIMBERWOLVES,
            ),
            # 2,7
            winsB=0,
            teamB=Matchup(
                winsA=1,
                teamA=Team.ROCKETS,
                winsB=2,
                teamB=Team.WARRIORS,
            ),
        ),
    ),
    # east
    winsB=0,
    teamB=Matchup(
        winsA=0,
        teamA=Matchup(
            # 1,8
            winsA=0,
            teamA=Matchup(
                winsA=3,
                teamA=Team.CAVALIERS,
                winsB=0,
                teamB=Team.HEAT,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=3,
                teamA=Team.PACERS,
                winsB=1,
                teamB=Team.BUCKS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=0,
            teamA=Matchup(
                winsA=3,
                teamA=Team.KNICKS,
                winsB=1,
                teamB=Team.PISTONS,
            ),
            # 2,7
            winsB=0,
            teamB=Matchup(
                winsA=3,
                teamA=Team.CELTICS,
                winsB=1,
                teamB=Team.MAGIC,
            ),
        ),
    ),
)

PLAYER_CHOICES = {
    "Justin": (
        Team.CELTICS,
        Team.LAKERS,
        Team.WARRIORS,
        Team.NUGGETS,
    ),
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
    "Nick": (
        Team.THUNDER,
        Team.CELTICS,
        Team.LAKERS,
        Team.BUCKS,
    ),
    "Gabe": (
        Team.WARRIORS,
        Team.TIMBERWOLVES,
        Team.NUGGETS,
        Team.CELTICS,
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
    "Gavin": (
        Team.THUNDER,
        Team.CELTICS,
        Team.CAVALIERS,
        Team.WARRIORS,
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
    queue.append(bracket.teamA)
    queue.append(bracket.teamB)

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
) -> Dict[str, int]:
    wins_for_each_team = gather_wins_per_team(bracket=bracket)
    ret = {}
    for player, choices in player_choices.items():
        points = sum([(wins_for_each_team[team] * team.points) for team in choices])
        ret[player] = points

    return ret


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


# Constructing all possible brackets is impossible when there are 15 games to play
# and 8 different variations of point breakdown between the team. Or in other words
# 8^15 or 10 trillion
def simulate_random_brackets(method: Literal["uniform", "geometric"]):
    player_wins = {player: 0 for player in PLAYER_CHOICES.keys()}
    simulations = 100_000
    for _ in range(simulations):
        bracket_copy = deepcopy(BRACKET_MATCHUP)
        if method == "uniform":
            random_uniform_bracket_fill(bracket_copy)
        elif method == "geometric":
            random_geometric_bracket_fill(bracket_copy)
        else:
            raise NotImplementedError(f"{method} not implemented")

        # TODO: account for ties
        player_scores = compute_all_scores_from_bracket(
            bracket=bracket_copy, player_choices=PLAYER_CHOICES
        )
        best_player = max(player_scores, key=lambda x: player_scores.get(x))
        player_wins[best_player] += 1

    print("\n \n")
    print(f"******{simulations} random {method} simulations results*****")
    # print(player_wins)

    headers = ("Player", "Wins", "Percentage %")
    data = [
        (player, wins, f"{100*wins/simulations:.1f}")
        for player, wins in player_wins.items()
    ]
    # sort by number of wins in simulation
    data.sort(key=lambda x: x[1], reverse=1)
    print_tabulate(header=headers, data=data)


# def debug_scoring():
#     player = "Jay"
#     score = compute_individual_score_from_bracket(
#         bracket=BRACKET_MATCHUP, choices=PLAYER_CHOICES[player]
#     )
#     print(f"{player} score: {score}")

if __name__ == "__main__":
    check_any_players_match()
    get_max_score_of_all_players()
    # simulate_random_brackets(method="uniform")
    simulate_random_brackets(method="geometric")
