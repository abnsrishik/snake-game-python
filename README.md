# Snake Game

Classic Snake built in Python with persistent high score tracking.
Eat food to grow, avoid walls and your own tail. High score saves 
between sessions via local file storage.

## Features

- Smooth OOP architecture — Snake, Food, Scoreboard as separate classes
- **Persistent high score** — saved to `data.txt`, survives after closing
- **Reset on collision** — game continues instead of ending; snake resets
- Wall collision and self-collision detection
- Arrow key controls

## Controls

| Key | Action |
|---|---|
| ↑ | Move up |
| ↓ | Move down |
| ← | Move left |
| → | Move right |

## How to Run

```bash
git clone https://github.com/abnsrishik/snake-game-python
cd snake-game-python
python main.py
```

No external dependencies. Uses Python's built-in `turtle` module.

## Architecture

| File | Class | Responsibility |
|---|---|---|
| `snake.py` | `Snake` | Segment management, movement, direction control, reset |
| `food.py` | `Food` | Random position spawning |
| `scoreboard.py` | `ScoreBoard` | Score tracking, high score read/write to `data.txt` |
| `main.py` | — | Game loop, collision detection, event binding |
| `data.txt` | — | Persists high score between sessions |

## What I Learned

- OOP inheritance from `Turtle` base class
- File I/O for persistent state (`open`, `read`, `write`)
- Collision detection using distance threshold
- Game reset logic without restarting the program
- Preventing reverse direction (can't go directly opposite)
