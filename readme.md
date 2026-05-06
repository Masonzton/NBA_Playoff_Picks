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

Results
---
Last Ran 5/06/2026

Running 100,000 random simulations using geometric method. All nba teams have an equal chance of winning
| Player     | Wins  | Percentage % | Average Score |
| ---------- | ----- | ------------ | ------------- |
| Kunal      | 52493 | 52.5         | 62.84773      |
| Gavin      | 31259 | 31.3         | 54.48295      |
| Sean       | 16168 | 16.2         | 50.61302      |
| Terminator | 80    | 0.1          | 46.3241       |

Distribution of ranking for each player. % chance they get this particular position

NOTE: does not account for tie's correctly, so it differs slightly from above
| Player     | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Justin     | 0.0  | 3.5  | 12.4 | 13.7 | 10.5 | 32.3 | 1.5  | 7.3  | 15.9 | 2.6  | 0.1  |
| Jack       | 0.0  | 0.0  | 0.5  | 3.6  | 5.1  | 5.7  | 34.0 | 5.1  | 17.4 | 28.5 | 0.0  |
| Kunal      | 55.1 | 29.8 | 4.1  | 3.2  | 5.9  | 2.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Nick       | 0.0  | 0.0  | 3.8  | 2.0  | 9.7  | 23.2 | 21.2 | 33.3 | 6.7  | 0.0  | 0.0  |
| Gabe       | 0.0  | 0.0  | 0.0  | 0.0  | 1.2  | 0.5  | 9.0  | 17.9 | 12.7 | 41.4 | 17.3 |
| Mike       | 0.0  | 0.0  | 0.0  | 0.0  | 0.1  | 0.5  | 2.4  | 4.3  | 3.5  | 7.1  | 82.2 |
| Mason      | 0.0  | 0.0  | 0.0  | 3.8  | 2.0  | 9.7  | 23.1 | 21.0 | 30.8 | 9.5  | 0.0  |
| Jay        | 0.1  | 7.5  | 24.8 | 45.1 | 10.1 | 4.4  | 1.7  | 3.8  | 2.6  | 0.1  | 0.0  |
| Sean       | 15.6 | 30.2 | 9.0  | 4.1  | 6.6  | 11.3 | 2.6  | 5.7  | 6.4  | 8.1  | 0.3  |
| Gavin      | 29.2 | 29.1 | 38.3 | 2.7  | 0.7  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Terminator | 0.0  | 0.0  | 7.1  | 21.8 | 48.1 | 10.3 | 4.5  | 1.6  | 3.8  | 2.7  | 0.1  |

Current Scores
| player     | W | Current Score | Max Score |
| ---------- | - | ------------- | --------- |
| Kunal      | * | 34            | 95        |
| Jay        | _ | 28            | 64        |
| Terminator | _ | 28            | 64        |
| Jack       | _ | 27            | 38        |
| Sean       | * | 27            | 74        |
| Gavin      | * | 27            | 80        |
| Justin     | _ | 25            | 57        |
| Nick       | _ | 23            | 57        |
| Mason      | _ | 23            | 57        |
| Gabe       | _ | 20            | 54        |
| Mike       | _ | 18            | 29        |
