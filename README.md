# Adaptive Rock-Paper-Scissors Bot

A Rock-Paper-Scissors bot built for freeCodeCamp's Machine Learning certification. The challenge: beat four different opponent bots, winning at least 60% of games against each.

## The approach

The bot doesn't know anything about its opponent going in. Instead, it watches how the match unfolds and looks for repeating patterns, specifically, it tracks both players' moves together (not just the opponent's) and searches for situations that have happened before, to predict what the opponent is likely to do next. Once it has a prediction, it just plays whatever beats it.

If it's never seen the current situation before, it falls back to countering the opponent's most frequent move overall, most bots aren't perfectly random, so this alone beats a lot of them.

## Why track both players' moves?

My first version only tracked the opponent's move history, and it worked great, except against one bot, Kris, which doesn't really have a pattern of its own. Kris just reacts to my last move. A model that only watches the opponent is blind to that. Tracking both players' moves together as one combined sequence fixed it.

## Results

Testing game against abbey...
Final results: {'p1': 606, 'p2': 267, 'tie': 127}
Player 1 win rate: 69.41580756013745%

.Testing game against kris...
Final results: {'p1': 981, 'p2': 13, 'tie': 6}
Player 1 win rate: 98.69215291750503%

.Testing game against mrugesh...
Final results: {'p1': 832, 'p2': 168, 'tie': 0}
Player 1 win rate: 83.2%

.Testing game against quincy...
Final results: {'p1': 985, 'p2': 4, 'tie': 11}
Player 1 win rate: 99.59555106167846%

All comfortably above the 60% requirement, confirmed by the project's official test suite.

## Running it

```
python main.py
```

`RPS.py` contains the bot. `RPS_game.py` (untouched, provided by freeCodeCamp) runs the matches and defines the opponent bots.

## What I actually learned

Honestly, I learned more about debugging than about Rock-Paper-Scissors itself. I ran into a sneaky Python bug where old data from a previous match kept leaking into the next one. I also had a bug where my "prediction" was really just repeating an old move instead of guessing the next one. And the biggest lesson: a strategy that crushes one opponent can completely fail against another, for reasons that only make sense once you actually understand how that opponent thinks.
