"""
Just going to compute if it is even possible for a certain person to win it all
"""
from enum import Enum
from typing import Union

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
            self.winner = teamA.get_team()
        elif winsB == 4:
            self.winner = teamB.get_team()
        else:
            self.winner = None
        
        # update child matchup to point up. Idk why
        self.parent = None
        if type(teamA) == Matchup:
            self.teamA.parent = self
        if type(teamB) == Matchup:
            self.teamB.parent = self
    
    def get_team(self) -> 'Team':
        return self.winner

# there are only 2^16 different possible combinations when only considering the straight up winner
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
                winsA=0,
                teamA=Team.THUNDER,
                winsB=0,
                teamB=Team.GRIZZLIES,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=0,
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
                winsB=0,
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
                winsA=0,
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
                winsA=0,
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

player1_choice = [
    Team.THUNDER,
    Team.GRIZZLIES,
    Team.NUGGETS,
    Team.CAVALIERS,
]


# construct all possible brackets
def construct_possible_brackets():
    pass

if __name__ == "__main__":
    construct_possible_brackets()
    pass