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
In the earlier rounds it is not feasible to calculate all 8^15 ~ 10 trillion brackets, but when there are less games left to play it is easier to just simulate all possible games.
Currently assuming each team has an equal chance of winning against each other.

Maximum scores are also computed

Results
---
Last Ran 5/10/2026 (After Knicks game)

Current Scores
| player     | Current Score | Max Score |
| ---------- | ------------- | --------- |
| Gavin      | 39            | 80        |
| Kunal      | 38            | 95        |
| Jay        | 36            | 64        |
| Terminator | 36            | 64        |
| Justin     | 33            | 57        |
| Jack       | 29            | 38        |
| Nick       | 27            | 57        |
| Mason      | 27            | 57        |
| Sean       | 27            | 74        |
| Gabe       | 24            | 54        |
| Mike       | 19            | 29        |

Running 100,000 random simulations using geometric method. All nba teams have an equal chance of winning
| Player     | Wins  | Percentage % | Average Score |
| ---------- | ----- | ------------ | ------------- |
| Gavin      | 72075 | 72.1         | 63.11436      |
| Kunal      | 26331 | 26.3         | 57.74355      |
| Sean       | 1594  | 1.6          | 38.2716       |

Distribution of ranking for each player. % chance they get this particular position

NOTE: I think this does not account for tie's correctly, so it differs slightly from above
| Player     | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Justin     | 0.0  | 12.5 | 22.2 | 14.8 | 21.8 | 13.0 | 0.2  | 11.5 | 4.0  | 0.0  | 0.0  |
| Jack       | 0.0  | 0.0  | 0.0  | 1.2  | 0.5  | 25.2 | 23.1 | 9.7  | 25.4 | 14.9 | 0.0  |
| Kunal      | 27.9 | 38.7 | 5.2  | 7.9  | 19.3 | 1.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Nick       | 0.0  | 0.0  | 0.5  | 0.2  | 13.1 | 25.7 | 34.5 | 25.2 | 0.8  | 0.0  | 0.0  |
| Gabe       | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 12.5 | 13.8 | 28.9 | 38.3 | 6.5  |
| Mike       | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.1  | 1.0  | 1.9  | 7.7  | 89.3 |
| Mason      | 0.0  | 0.0  | 0.0  | 0.5  | 0.2  | 13.1 | 25.7 | 34.3 | 24.2 | 2.0  | 0.0  |
| Jay        | 0.0  | 19.4 | 38.2 | 35.2 | 5.9  | 0.5  | 0.6  | 0.2  | 0.0  | 0.0  | 0.0  |
| Sean       | 1.7  | 10.0 | 4.3  | 2.7  | 3.7  | 15.2 | 2.9  | 3.8  | 14.5 | 37.1 | 4.2  |
| Gavin      | 70.4 | 19.4 | 10.2 | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Terminator | 0.0  | 0.0  | 19.3 | 37.6 | 35.5 | 6.3  | 0.5  | 0.5  | 0.2  | 0.0  | 0.0  |


Team Comparison's
----

How many teams each player has in common
| Player     | Justin | Jack | Kunal | Nick | Gabe | Mike | Mason | Jay | Sean | Gavin | Terminator |
| ---------- | ------ | ---- | ----- | ---- | ---- | ---- | ----- | --- | ---- | ----- | ---------- |
| Justin     | 4      | 2    | 1     | 3    | 2    | 2    | 2     | 3   | 1    | 2     | 3          |
| Jack       | 2      | 4    | 2     | 2    | 2    | 1    | 3     | 1   | 1    | 1     | 1          |
| Kunal      | 1      | 2    | 4     | 2    | 2    | 0    | 3     | 1   | 1    | 2     | 1          |
| Nick       | 3      | 2    | 2     | 4    | 3    | 2    | 3     | 3   | 1    | 2     | 3          |
| Gabe       | 2      | 2    | 2     | 3    | 4    | 2    | 3     | 2   | 1    | 2     | 2          |
| Mike       | 2      | 1    | 0     | 2    | 2    | 4    | 1     | 2   | 1    | 0     | 2          |
| Mason      | 2      | 3    | 3     | 3    | 3    | 1    | 4     | 2   | 1    | 2     | 2          |
| Jay        | 3      | 1    | 1     | 3    | 2    | 2    | 2     | 4   | 1    | 2     | 4          |
| Sean       | 1      | 1    | 1     | 1    | 1    | 1    | 1     | 1   | 4    | 0     | 1          |
| Gavin      | 2      | 1    | 2     | 2    | 2    | 0    | 2     | 2   | 0    | 4     | 2          |
| Terminator | 3      | 1    | 1     | 3    | 2    | 2    | 2     | 4   | 1    | 2     | 4          |


Each players most common matching's
| Player     | # of Teams in Common | Matching Players                                                                  |
| ---------- | -------------------- | --------------------------------------------------------------------------------- |
| Jay        | 4                    | ['Jay', 'Terminator']                                                             |
| Terminator | 4                    | ['Jay', 'Terminator']                                                             |
| Justin     | 3                    | ['Nick', 'Jay', 'Terminator']                                                     |
| Jack       | 3                    | ['Mason']                                                                         |
| Kunal      | 3                    | ['Mason']                                                                         |
| Nick       | 3                    | ['Justin', 'Gabe', 'Mason', 'Jay', 'Terminator']                                  |
| Gabe       | 3                    | ['Nick', 'Mason']                                                                 |
| Mason      | 3                    | ['Jack', 'Kunal', 'Nick', 'Gabe']                                                 |
| Mike       | 2                    | ['Justin', 'Nick', 'Gabe', 'Jay', 'Terminator']                                   |
| Gavin      | 2                    | ['Justin', 'Kunal', 'Nick', 'Gabe', 'Mason', 'Jay', 'Terminator']                 |
| Sean       | 1                    | ['Justin', 'Jack', 'Kunal', 'Nick', 'Gabe', 'Mike', 'Mason', 'Jay', 'Terminator'] |


How much was each team chosen by players
| Team           | # Chosen |
| -------------- | -------- |
| NUGGETS        | 9        |
| THUNDER        | 7        |
| CAVALIERS      | 7        |
| ROCKETS        | 5        |
| KNICKS         | 4        |
| HAWKS          | 3        |
| TIMBERWOLVES   | 2        |
| CELTICS        | 2        |
| SUNS           | 1        |
| LAKERS         | 1        |
| SPURS          | 1        |
| PISTONS        | 1        |
| MAGIC          | 1        |
| TRAIL_BLAZERS  | 0        |
| RAPTORS        | 0        |
| SEVENTY_SIXERS | 0        |