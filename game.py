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
                teamB=Team.GRIZZLIES,
            ),
            # 4,5 
            winsB=3, # Nuggets
            teamB=Matchup(
                winsA=4,
                teamA=Team.NUGGETS,
                winsB=3,
                teamB=Team.CLIPPERS,
            ),
        ),
        winsB=0, # Timberwolves
        teamB=Matchup(
            # 3,6
            winsA=4, # Timberwolves
            teamA=Matchup(
                winsA=1,
                teamA=Team.LAKERS,
                winsB=4,
                teamB=Team.TIMBERWOLVES,
            ),
            # 2,7
            winsB=1, # Warriors
            teamB=Matchup(
                winsA=3,
                teamA=Team.ROCKETS,
                winsB=4,
                teamB=Team.WARRIORS,
            ),
        ),
    ),
    # east
    winsB=0,
    teamB=Matchup(
        winsA=0, # Pacers
        teamA=Matchup(
            # 1,8
            winsA=1, # Cavaliers
            teamA=Matchup(
                winsA=4,
                teamA=Team.CAVALIERS,
                winsB=0,
                teamB=Team.HEAT,
            ),
            # 4,5
            winsB=4, # Pacers
            teamB=Matchup(
                winsA=4,
                teamA=Team.PACERS,
                winsB=1,
                teamB=Team.BUCKS,
            ),
        ),
        winsB=0, # Knicks
        teamB=Matchup(
            # 3,6
            winsA=4, # Knicks
            teamA=Matchup(
                winsA=4,
                teamA=Team.KNICKS,
                winsB=2,
                teamB=Team.PISTONS,
            ),
            # 2,7
            winsB=2, # Celtics
            teamB=Matchup(
                winsA=4,
                teamA=Team.CELTICS,
                winsB=1,
                teamB=Team.MAGIC,
            ),
        ),
    ),
)
