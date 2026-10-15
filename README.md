# Snake AI with Deep Q-Learning (Python • PyTorch • Pygame)

A Deep Q-Network (DQN) agent that learns to play Snake from reward alone, with no hand-written strategy.
Built by following [this tutorial](https://www.youtube.com/watch?v=L8ypSXwyBds), then extended with **TODO: your extension, e.g. an ablation of replay and ε-decay**.

![Training curve](results/scores.png)
<!-- TODO: save the plotter.py output to results/scores.png -->

## Results

| Metric | Value |
|---|---|
| Episodes trained | TODO |
| Mean score (last 100 games) | TODO |
| Record score | TODO |
| Seeds | TODO (use 5 or more) |

<!-- Only add the sentence below if it is true, e.g. "Replay lifts the mean score from X to Y." -->

## How it works

**Environment.** Grid-based Snake in Pygame. Each step the agent picks one action: TODO (e.g. 3 relative moves: straight, turn left, turn right).

**State** (TODO: size, e.g. 11 binary features):
- danger straight / left / right
- current direction
- food location relative to the head (left / right / up / down)

**Reward:** TODO (e.g. +10 for food, −10 for collision, 0 otherwise).

**Agent.**
- Network: TODO (e.g. MLP 11 → 256 → 3).
- Learning target, from the Bellman equation:
  `y = r + γ · max_a' Q(s', a')`, with loss `(y − Q(s, a))²`.
- Exploration: ε-greedy, with ε decaying over games (TODO: schedule).
- Experience replay: buffer of TODO transitions, mini-batches of TODO.
- Hyperparameters: lr = TODO, γ = TODO.

## Run it

```bash
git clone https://github.com/JHDng/ML_Snake.git
cd ML_Snake
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt # TODO: add this file (torch, pygame, numpy, matplotlib)
python agent.py                 # trains with live visualisation
```

## Repository layout

| Path | Purpose |
|---|---|
| `agent.py` | Training loop, ε-greedy policy, replay memory |
| `model.py` | Q-network and optimisation step |
| `snake_game_pkg/` | Pygame environment |
| `plotter.py` | Live and saved score plots |

## Limitations

- Hand-crafted state, so it does not learn from pixels.
- TODO: single run vs. multiple seeds; no target network (if true).
- Final performance depends on the random seed.

## Ideas for future work

- Double DQN, dueling networks, prioritised replay.
- A CNN on raw frames instead of engineered features.
- Reward shaping (e.g. distance-to-food) and its effect on stability.

## References

- Tutorial: [Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake](https://www.youtube.com/watch?v=L8ypSXwyBds)
- Mnih et al., *Human-level control through deep reinforcement learning*, Nature, 2015.
- Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.
