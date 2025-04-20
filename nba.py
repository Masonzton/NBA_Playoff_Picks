"""
Just going to compute if it is even possible for a certain person to win it all
"""
from enum import Enum
from typing import Union, Tuple, List
from copy import deepcopy
from functools import cached_property

class Team(Enum):
    THUNDER =      ("THUNDER", 1)
    GRIZZLIES =    ("GRIZZLIES", 8)
    NUGGETS =      ("NUGGETS", 4)
    CLIPPERS =     ("CLIPPERS", 5)
    LAKERS =       ("LAKERS", 3)
    TIMBERWOLVES = ("TIMBERWOLVES", 6)
    ROCKETS =      ("ROCKETS", 2)
    WARRIORS =     ("WARRIORS", 7)
    CAVALIERS =    ("CAVALIERS", 1)
    HEAT =         ("HEAT", 8)
    PACERS =       ("PACERS", 4)
    BUCKS =        ("BUCKS", 5)
    KNICKS =       ("KNICKS", 3)
    PISTONS =      ("PISTONS", 6)
    CELTICS =      ("CELTICS", 2)
    MAGIC =        ("MAGIC", 7)

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

    def get_team(self) -> 'Team':
        return self
    

class Matchup:
    def __init__(
        self,
        teamA: Union[Team, 'Matchup'],
        teamB: Union[Team, 'Matchup'],
        winsA:int,
        winsB:int,
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
    
    def get_team(self) -> 'Team':
        """Updates winner and returns winner"""
        if self.winsA == 4:
            self._winner = self.teamA.get_team()
        elif self.winsB == 4:
            self._winner = self.teamB.get_team()
        return self._winner

# bracket breakdown
BRACKET_MATCHUP = Matchup(
    # west
    winsA=0,
    teamA=Matchup(
        winsA=0,
        teamA=Matchup(
            # 1,8
            winsA=0,
            teamA=Matchup(
                winsA=1,
                teamA=Team.THUNDER,
                winsB=0,
                teamB=Team.GRIZZLIES,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=1,
                teamA=Team.NUGGETS,
                winsB=0,
                teamB=Team.CLIPPERS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=0,
            teamA=Matchup(
                winsA=0,
                teamA=Team.LAKERS,
                winsB=1,
                teamB=Team.TIMBERWOLVES,
            ),
            #2,7
            winsB=0,
            teamB=Matchup(
                teamA=Team.ROCKETS,
                teamB=Team.WARRIORS,
                winsA=0,
                winsB=0,
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
                winsA=0,
                teamA=Team.CAVALIERS,
                winsB=0,
                teamB=Team.HEAT,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=1,
                teamA=Team.PACERS,
                winsB=0,
                teamB=Team.BUCKS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=0,
            teamA=Matchup(
                winsA=1,
                teamA=Team.KNICKS,
                winsB=0,
                teamB=Team.PISTONS,
            ),
            #2,7
            winsB=0,
            teamB=Matchup(
                winsA=0,
                teamA=Team.CELTICS,
                winsB=0,
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

# construct all possible brackets is impossible
# there are fucking 6^15 ~ 400 billion damn combinations

def check_any_players_match():
    for playerA, choiceA in PLAYER_CHOICES.items():
        for playerB, choiceB in PLAYER_CHOICES.items():
            if playerA == playerB:
                continue
            
            if all([choice in choiceB for choice in choiceA]):
                print(f"{playerA} and {playerB} have the same choice of teams")

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
    if scoreA > scoreB:
        bracket.winsA = 4
        bracket.winsB = 3
    else:
        bracket.winsB = 4
        bracket.winsA = 3

def compute_score_from_bracket(bracket: Matchup, choices: Tuple[Team, Team, Team, Team]) -> int:
    # search the tree and accumulates points for each favorable score
    # bfs
    queue : List[Matchup] = []
    queue.append(bracket.teamA)
    queue.append(bracket.teamB)
    points = 0
    while queue:
        m = queue.pop(0)

        # act on m
        # add up points for teams that are apart of this player's choice
        teamA = m.teamA.get_team()
        if teamA is not None and teamA in choices:
            points += teamA.points * m.winsA
        teamB = m.teamB.get_team()
        if teamB is not None and teamB in choices:
            points += teamB.points * m.winsB
        
        # add more matchup's to the queue
        if type(m.teamA) == Matchup:
            queue.append(m.teamA)
            queue.append(m.teamB)
    
    return points

def get_max_score_of_all_players():
    for player, choices in PLAYER_CHOICES.items():
        ideal_bracket = deepcopy(BRACKET_MATCHUP)
        # depth first recursively fill out the bracket in a greedy way
        greedy_fill_bracket(ideal_bracket, choices)
        score = compute_score_from_bracket(bracket=ideal_bracket, choices=choices)
        print(f"{player} max score is {score}")

if __name__ == "__main__":
    check_any_players_match()
    get_max_score_of_all_players()
    pass