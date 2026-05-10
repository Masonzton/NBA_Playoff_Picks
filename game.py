"""
This stores the current state of the NBA playoffs, not the easiest to edit...
"""

from my_types import Team, Matchup

# bracket breakdown
BRACKET_MATCHUP = Matchup(
    # west
    winsA=0,
    teamA=Matchup(
        winsA=0,
        teamA=Matchup(
            # 1,8
            winsA=3, # Thunder
            teamA=Matchup(
                winsA=4,
                teamA=Team.THUNDER,
                winsB=0,
                teamB=Team.SUNS,
            ),
            # 4,5 
            winsB=0, # Lakers
            teamB=Matchup(
                winsA=4,
                teamA=Team.LAKERS,
                winsB=2,
                teamB=Team.ROCKETS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=1, # TIMBERWOLVES
            teamA=Matchup(
                winsA=2,
                teamA=Team.NUGGETS,
                winsB=4,
                teamB=Team.TIMBERWOLVES,
            ),
            # 2,7
            winsB=2, # SPURS
            teamB=Matchup(
                winsA=4,
                teamA=Team.SPURS,
                winsB=1,
                teamB=Team.TRAIL_BLAZERS,
            ),
        ),
    ),
    # east
    winsB=0,
    teamB=Matchup(
        winsA=0,
        teamA=Matchup(
            # 1,8
            winsA=2, # PISTONS
            teamA=Matchup(
                winsA=4,
                teamA=Team.PISTONS,
                winsB=3,
                teamB=Team.MAGIC,
            ),
            # 4,5
            winsB=1, # CAVALIERS
            teamB=Matchup(
                winsA=4,
                teamA=Team.CAVALIERS,
                winsB=3,
                teamB=Team.RAPTORS,
            ),
        ),
        winsB=0, # KNICKS
        teamB=Matchup(
            # 3,6
            winsA=4, # KNICKS
            teamA=Matchup(
                winsA=4,
                teamA=Team.KNICKS,
                winsB=2,
                teamB=Team.HAWKS,
            ),
            # 2,7
            winsB=0, # SEVENTY_SIXERS
            teamB=Matchup(
                winsA=3,
                teamA=Team.CELTICS,
                winsB=4,
                teamB=Team.SEVENTY_SIXERS,
            ),
        ),
    ),
)
