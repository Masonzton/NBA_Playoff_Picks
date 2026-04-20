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
            winsA=0,
            teamA=Matchup(
                winsA=0,
                teamA=Team.THUNDER,
                winsB=0,
                teamB=Team.SUNS,
            ),
            # 4,5 
            winsB=0,
            teamB=Matchup(
                winsA=0,
                teamA=Team.LAKERS,
                winsB=0,
                teamB=Team.ROCKETS,
            ),
        ),
        winsB=0,
        teamB=Matchup(
            # 3,6
            winsA=0,
            teamA=Matchup(
                winsA=0,
                teamA=Team.NUGGETS,
                winsB=0,
                teamB=Team.TIMBERWOLVES,
            ),
            # 2,7
            winsB=0,
            teamB=Matchup(
                winsA=0,
                teamA=Team.SPURS,
                winsB=0,
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
            winsA=0,
            teamA=Matchup(
                winsA=0,
                teamA=Team.PISTONS,
                winsB=0,
                teamB=Team.MAGIC,
            ),
            # 4,5
            winsB=0,
            teamB=Matchup(
                winsA=0,
                teamA=Team.CAVALIERS,
                winsB=0,
                teamB=Team.RAPTORS,
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
                teamB=Team.HAWKS,
            ),
            # 2,7
            winsB=0,
            teamB=Matchup(
                winsA=0,
                teamA=Team.CELTICS,
                winsB=0,
                teamB=Team.SEVENTY_SIXERS,
            ),
        ),
    ),
)
