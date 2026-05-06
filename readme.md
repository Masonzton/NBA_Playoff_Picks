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
Running 10,000 random simulations using geometric method
| Player     | Wins | Percentage % | Average Score |
| ---------- | ---- | ------------ | ------------- |
| Kunal      | 5245 | 52.5         | 62.878        |
| Gavin      | 3130 | 31.3         | 54.5121       |
| Sean       | 1621 | 16.2         | 50.5902       |
| Terminator | 4    | 0.0          | 46.3016       |
| Justin     | 0    | 0.0          | 40.8342       |
| Jack       | 0    | 0.0          | 32.2964       |
| Nick       | 0    | 0.0          | 36.0602       |
| Gabe       | 0    | 0.0          | 33.0602       |
| Mike       | 0    | 0.0          | 23.285        |
| Mason      | 0    | 0.0          | 36.0602       |
| Jay        | 0    | 0.0          | 46.3016       |

Distribution of ranking for each player
| Player     | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Justin     | 0.0  | 3.5  | 12.4 | 14.6 | 10.1 | 31.8 | 1.3  | 7.5  | 16.0 | 2.6  | 0.1  |
| Jack       | 0.0  | 0.0  | 0.5  | 3.5  | 5.6  | 5.7  | 34.1 | 5.2  | 17.2 | 28.3 | 0.0  |
| Kunal      | 55.1 | 29.8 | 4.1  | 3.1  | 5.8  | 2.1  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Nick       | 0.0  | 0.0  | 3.8  | 2.3  | 9.6  | 23.1 | 20.8 | 33.7 | 6.7  | 0.0  | 0.0  |
| Gabe       | 0.0  | 0.0  | 0.0  | 0.0  | 1.2  | 0.5  | 9.3  | 17.7 | 12.5 | 40.9 | 17.9 |
| Mike       | 0.0  | 0.0  | 0.0  | 0.1  | 0.1  | 0.5  | 2.4  | 4.3  | 3.6  | 7.5  | 81.5 |
| Mason      | 0.0  | 0.0  | 0.0  | 3.8  | 2.3  | 9.6  | 23.1 | 20.5 | 31.1 | 9.7  | 0.0  |
| Jay        | 0.0  | 7.4  | 24.9 | 44.3 | 10.4 | 4.8  | 1.9  | 3.6  | 2.6  | 0.1  | 0.0  |
| Sean       | 15.8 | 29.6 | 9.5  | 4.0  | 6.7  | 11.3 | 2.2  | 5.6  | 6.7  | 8.2  | 0.3  |
| Gavin      | 29.1 | 29.6 | 37.9 | 2.6  | 0.8  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  | 0.0  |
| Terminator | 0.0  | 0.0  | 7.0  | 21.8 | 47.3 | 10.6 | 4.9  | 1.8  | 3.6  | 2.7  | 0.1  |
