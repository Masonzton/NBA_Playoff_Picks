# how many times to run the simulation. takes about 2 seconds per 10_000 simulations
SIMULATION_TO_RUN = 100_000

# Matchup odds between each two possible teams that can play together
# -1 are filled out automatically based on reciprocal odds or are teams playing themselves
# probability indicates odds that teamA on the left will beat teamB above. For example, Thunder have a 75% chance of beating grizzlies each game
MATCHUP_ODDS = (
 # (               THUNDER SUNS  LAKERS ROCKETS NUGGETS TIMBERWOLVES SPURS TRAIL_BLAZERS PISTONS   MAGIC CAVALIERS RAPTORS KNICKS HAWKS CELTICS SEVENTY_SIXERS
("THUNDER",        -1,     0.5,  0.5,    0.5,     0.5,   0.5,         0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("SUNS",           -1,     -1,   0.5,    0.5,     0.5,   0.5,         0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("LAKERS",         -1,     -1,   -1,     0.5,     0.5,   0.5,         0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("ROCKETS",        -1,     -1,   -1,     -1,      0.5,   0.5,         0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("NUGGETS",        -1,     -1,   -1,     -1,      -1,    0.5,         0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("TIMBERWOLVES",   -1,     -1,   -1,     -1,      -1,    -1,          0.5,    0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("SPURS",          -1,     -1,   -1,     -1,      -1,    -1,          -1,     0.5,       0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("TRAIL_BLAZERS",  -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        0.5,      0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("PISTONS",        -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       0.5,  0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("MAGIC",          -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   0.5,      0.5,    0.5,   0.5,  0.5,    0.5,),
("CAVALIERS",      -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       0.5,    0.5,   0.5,  0.5,    0.5,),
("RAPTORS",        -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       -1,     0.5,   0.5,  0.5,    0.5,),
("KNICKS",         -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       -1,     -1,    0.5,  0.5,    0.5,),
("HAWKS",          -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       -1,     -1,    -1,   0.5,    0.5,),
("CELTICS",        -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       -1,     -1,    -1,   -1,     0.5,),
("SEVENTY_SIXERS", -1,     -1,   -1,     -1,      -1,    -1,          -1,     -1,        -1,       -1,   -1,       -1,     -1,    -1,   -1,     -1, ),
)
 