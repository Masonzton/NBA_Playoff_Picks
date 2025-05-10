from enum import Enum, auto
from typing import Union
from random import choices as random_choice
from functools import cached_property
from config import MATCHUP_ODDS


times_index_is_called = 0

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

    @cached_property
    def index(self) -> int:
        global times_index_is_called
        length_of_class = len(list(self.__class__))
        times_index_is_called += 1
        value = list(self.__class__).index(self)
        assert value >= 0
        assert value < length_of_class
        assert times_index_is_called <= length_of_class
        return value
    
    def debug_print(self) -> int:
        print(times_index_is_called)

    def get_team(self) -> "Team":
        return self


TEAMS_IN_ORDER = [team for team in Team]
TEAM_TO_INDEX = {team: idx for idx, team in enumerate(TEAMS_IN_ORDER)}


def get_matchup_odds(teamA: Team, teamB: Team):
    """
    Get odds that teamA beats teamB
    """
    # note that we need to add 1 when accessing the second index due to the first entry being an enum
    idxA = TEAM_TO_INDEX[teamA]
    idxB = TEAM_TO_INDEX[teamB]
    prob = MATCHUP_ODDS[idxA][idxB + 1]
    # if this is a negative one, then use the other side of the table
    if prob == -1:
        prob = 1.0 - MATCHUP_ODDS[idxB][idxA + 1]

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
        if self._winner is None:
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

        team = random_choice(
            population=["a", "b"], weights=[probability_A_win, (1 - probability_A_win)]
        )[0]
        if team == "a":
            self.winsA += 1
        elif team == "b":
            self.winsB += 1
        else:
            raise ValueError(f"Unexpected random choice {team}")
