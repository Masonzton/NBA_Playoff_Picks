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
Last Ran 4/30/2025 10:00 pm PST
I removed the terminator to see the odds without it
```
player  W  Current Score  Max Score
-----------------------------------
Gabe    *  34             103      
Jack    *  30             112      
Kunal   *  28             112      
Jay     _  26             107      
Mason   _  25             96       
Justin  _  24             84       
Mike    _  24             95       
Gavin   *  24             82       
Sean    _  18             81       
Nick    _  13             29 

******Running 1,000,000 random simulations using geometric method*****
Player  Wins    Percentage %
------------------------------
Gabe    710708  71.1        
Jack    178557  17.9        
Kunal   107814  10.8        
Gavin   2921    0.3         
Justin  0       0.0         
Nick    0       0.0         
Mike    0       0.0         
Mason   0       0.0         
Jay     0       0.0         
Sean    0       0.0         
encountered 27,624 ties or 2.8%

Distribution of ranking for each player
Player  1     2     3     4     5     6     7     8     9     10  
----------------------------------------------------
Justin  0.0   17.3  11.8  13.7  16.9  13.2  0.5   6.6   20.0  0.0 
Jack    20.3  31.0  21.5  12.3  12.4  2.3   0.2   0.1   0.0   0.0 
Kunal   11.0  28.8  27.3  20.4  12.5  0.0   0.0   0.0   0.0   0.0 
Nick    0.0   0.0   0.0   0.0   0.0   0.0   0.0   0.8   15.6  83.6
Gabe    68.5  10.9  5.1   5.3   0.9   5.4   4.0   0.0   0.0   0.0 
Mike    0.0   0.0   0.0   3.5   9.9   10.7  32.8  43.1  0.0   0.0 
Mason   0.0   0.1   4.2   10.4  12.1  36.1  37.0  0.0   0.0   0.0 
Jay     0.0   4.3   16.1  17.7  12.2  13.6  8.0   27.2  0.8   0.0 
Sean    0.0   0.0   0.0   0.0   0.0   3.6   9.1   7.4   63.5  16.4
Gavin   0.2   7.6   14.0  16.8  23.1  15.2  8.4   14.7  0.1   0.0 

```

Knock Outs
---
For most cases it seems like you can kind tell why a certain players chance has gone to 0. It is usually because another player's choice is very similar and the only differing team got knocked out.


```
What % of times each player wins against another player, useful for seeing which player 'knocked out' each other
Player  Justin  Jack  Kunal  Nick   Gabe  Mike   Mason  Jay    Sean   Gavin
-------------------------------------------------------------
Justin  0.0     23.2  29.1   100.0  0.0   73.5   70.1   49.2   79.8   39.2 
Jack    74.6    0.0   57.6   100.0  26.2  99.1   98.0   79.5   100.0  76.8 
Kunal   67.1    38.2  0.0    100.0  20.2  100.0  100.0  100.0  100.0  72.8 
Nick    0.0     0.0   0.0    0.0    0.0   0.0    0.0    0.5    15.5   0.0  
Gabe    100.0   72.3  78.0   100.0  0.0   90.9   88.6   85.0   96.1   98.0 
Mike    26.4    0.3   0.0    100.0  9.1   0.0    0.0    27.0   100.0  19.6 
Mason   26.4    0.9   0.0    100.0  9.1   100.0  0.0    38.5   100.0  22.3 
Jay     48.4    17.5  0.0    99.3   14.1  61.5   54.9   0.0    100.0  48.1 
Sean    19.2    0.0   0.0    82.4   3.4   0.0    0.0    0.0    0.0    11.6 
Gavin   58.7    19.8  23.4   100.0  1.4   77.7   73.6   49.4   88.0   0.0
```