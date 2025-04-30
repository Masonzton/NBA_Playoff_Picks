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
Last Ran 4/29/2025 11:00 pm PST
```
player      W  Current Score  Max Score
---------------------------------------
Gabe        *  31             103      
Terminator  *  31             109      
Jack        *  30             112      
Kunal       _  28             112      
Jay         *  26             119      
Mason       _  25             96       
Justin      *  24             96       
Mike        *  24             107      
Gavin       *  24             82       
Sean        _  18             81       
Nick        _  13             50       

How many teams each player has in common
Player      Justin  Jack  Kunal  Nick  Gabe  Mike  Mason  Jay  Sean  Gavin  Terminator
----------------------------------------------------------------------
Justin      4       1     2      2     3     3     2      2    1     2      1         
Jack        1       4     2      1     1     2     2      2    2     2      3         
Kunal       2       2     4      1     2     3     3      3    2     2      2         
Nick        2       1     1      4     1     2     2      1    0     2      1         
Gabe        3       1     2      1     4     2     2      1    1     2      2         
Mike        3       2     3      2     2     4     3      3    2     2      2         
Mason       2       2     3      2     2     3     4      2    2     2      2         
Jay         2       2     3      1     1     3     2      4    2     1      2         
Sean        1       2     2      0     1     2     2      2    4     1      2         
Gavin       2       2     2      2     2     2     2      1    1     4      2         
Terminator  1       3     2      1     2     2     2      2    2     2      4         

How much was each team chosen by players
Team          # Chosen
--------------------------
THUNDER       4       
GRIZZLIES     1       
NUGGETS       2       
CLIPPERS      7       
LAKERS        4       
TIMBERWOLVES  2       
ROCKETS       0       
WARRIORS      10      
CAVALIERS     1       
HEAT          1       
PACERS        1       
BUCKS         2       
KNICKS        2       
PISTONS       0       
CELTICS       7       
MAGIC         0       

******Running 1,000,000 random simulations using geometric method*****
Player      Wins    Percentage %
----------------------------------
Gabe        510819  51.1        
Terminator  235688  23.6        
Jack        109069  10.9        
Jay         50917   5.1         
Justin      47904   4.8         
Kunal       36300   3.6         
Mike        5479    0.5         
Gavin       3824    0.4         
Nick        0       0.0         
Mason       0       0.0         
Sean        0       0.0         
encountered 49,323 ties or 4.9%

Without Terminator
******Running 1,000,000 random simulations using geometric method*****
Player  Wins    Percentage %
------------------------------
Gabe    622917  62.3        
Jack    176395  17.6        
Kunal   86374   8.6         
Jay     55898   5.6         
Justin  47803   4.8         
Mike    5941    0.6         
Gavin   4672    0.5         
Nick    0       0.0         
Mason   0       0.0         
Sean    0       0.0         
encountered 37,377 ties or 3.7%
```