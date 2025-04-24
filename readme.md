The NBA playoff bracket game I am playing is as follows. 
Each participant is to pick 4 teams. Each team you pick will get your points for each game won according to their seed
- 1st and 2nd seed teams 1 points
- 3rd and 4th seed teams 2 points
- 5th and 6th seed teams 3 points
- 7th and 8th seed teams 4 points

Picks of teams will be in order. The tie breaker is based on who's first choice team gained more points for them.

For example, if you choose a 3rd seed team and they win 4 of the games in the first round but only 2 of the games in the second round, they would win you (6 games) * (2 points per game) = 12 points

The nba.py script is meant to determine if at any point a player is "out" meaning that they there is no possible combination of wins that will secure a first place victory for them.

For the first round, it is isn't feasible or necessary to iterate over all 8^15 ~ 10 trillion potential brackets.
Instead a monte carlo like or random simulation is employed to confirm that indeed any person has the possibility to win.
You can also get a sense of the distribution of how many different ways a each person could win. However, this just heavily favors people who picked a lot of lower seeds since it doesn't consider the inherent lower odds of them winning games.

I also computed the maximum score each person just to see.

When the number of games left to play is smaller, the number of potential brackets is a lot more tractable to iterate over.