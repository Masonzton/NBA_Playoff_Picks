# how many times to run the simulation. takes about 2 seconds per 10_000 simulations
SIMULATION_TO_RUN = 10_000

# Matchup odds between each two possible teams that can play together
# -1 are filled out automatically based on reciprocal odds or are teams playing themselves
# probability indicates odds that teamA on the left will beat teamB above. For example, Thunder have a 75% chance of beating grizzlies each game
MATCHUP_ODDS = (
 # (             THUNDER GRIZZLIES NUGGETS CLIPPERS LAKERS TIMBERWOLVES ROCKETS WARRIORS CAVALIERS HEAT PACERS BUCKS KNICKS PISTONS CELTICS MAGIC
("THUNDER",      -1,     0.75,     0.5,    0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("GRIZZLIES",    -1,     -1,       0.5,    0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("NUGGETS",      -1,     -1,       -1,     0.5,     0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("CLIPPERS",     -1,     -1,       -1,     -1,      0.5,   0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("LAKERS",       -1,     -1,       -1,     -1,      -1,    0.5,         0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("TIMBERWOLVES", -1,     -1,       -1,     -1,      -1,    -1,          0.5,    0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("ROCKETS",      -1,     -1,       -1,     -1,      -1,    -1,          -1,     0.5,     0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("WARRIORS",     -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      0.5,      0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("CAVALIERS",    -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       0.5, 0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("HEAT",         -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  0.5,   0.5,  0.5,   0.5,    0.5,    0.5,),
("PACERS",       -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    0.5,  0.5,   0.5,    0.5,    0.5,),
("BUCKS",        -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   0.5,   0.5,    0.5,    0.5,),
("KNICKS",       -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    0.5,    0.5,    0.5,),
("PISTONS",      -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     0.5,    0.5,),
("CELTICS",      -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     -1,     0.5,),
("MAGIC",        -1,     -1,       -1,     -1,      -1,    -1,          -1,     -1,      -1,       -1,  -1,    -1,   -1,    -1,     -1,     -1, ),
)
