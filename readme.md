Rules of the game
---
The NBA playoff bracket game I am playing is as follows. 
Each participant is to pick 4 teams. Each team you pick will get your points for each game won according to their seed
- 1st and 2nd seed teams 1 points
- 3rd and 4th seed teams 2 points
- 5th and 6th seed teams 3 points
- 7th and 8th seed teams 4 points

Picks of teams will be in order. The tie breaker is based on who's first choice team gained more points for them.

For example, if you choose a 3rd seed team and they win 4 of the games in the first round but only 2 of the games in the second round, they would win you (6 games) * (2 points per game) = 12 points

Basic Usage
---
You must have python installed and then you can just run

```python3 nba.py```

You can edit ```config.py``` to set the odds for each possible matchup yourself. All odds default to 50/50.

```game.py``` stores the current state of the NBA playoffs, that I'll manually edit every now and then. Not the easiest to edit...

Running the script will make 10,000 copies of the current bracket, simulate every single matchup according to the odds selected, and keep a running total of who wins each simulated bracket.
In the earlier rounds it is not feasible to calculate all 8^15 ~ 10 trillion brackets, but maybe later I will do a more exhaustive approach, when there's less possibilities.

Maximum scores are also computed

Insights
---
Here are some things I have noticed playing around with this.

1) the timberwolves was an amazing pick. They were only a few people that chose that team, they were a low seed, and they are doing well in their series

2) If the bucks lose the next Game, Mason and Nick have almost no chance of winning (I think literally impossible). I tried around 3 million different simulation but I couldn't find the winning bracket. So at most a 1 in 3 million chance of winning.
But, I believe the bucks can pull it off!!!

Results
---
Last Ran 5/18/2025 10:11 am PST
```
player  W  Current Score  Max Score
-----------------------------------
Gabe    *  64             96       
Jack    *  52             76       
Kunal   *  51             67       
Jay     _  47             63       
Justin  _  42             60       
Gavin   _  38             47       
Mason   _  38             38       
Mike    _  37             37       
Sean    _  29             29       
Nick    _  18             27       

1,024 possible brackets left
Player  Wins  Percentage %
----------------------------
Gabe    890   86.9        
Jack    115   11.2        
Kunal   19    1.9         
Gavin   0     0.0         
Justin  0     0.0         
Nick    0     0.0         
Mike    0     0.0         
Mason   0     0.0         
Jay     0     0.0         
Sean    0     0.0
```
