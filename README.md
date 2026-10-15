# Snake AI with Deep Q-Learning (Python • PyTorch • Pygame)

A learning project in which a Deep Q-Network (DQN) agent learns to play Snake from game-play reward. It follows the tutorial [Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake](https://www.youtube.com/watch?v=L8ypSXwyBds) and is a reproduction of it, not original research.

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Getting Started](#getting-started)
4. [Implementation Details](#implementation-details)
5. [Results](#results)
6. [Possible Extensions](#possible-extensions)
7. [Acknowledgements](#acknowledgements)

## Features

- Snake game with movement, growth and collision detection
- DQN agent with experience replay and ε-greedy exploration
- Configurable learning rate, discount factor (γ) and exploration rate (ε)
- Real-time Pygame visualisation of training
- Training plots (`plotter.py`)

## Tech Stack

- **Python 3.7**
- **PyTorch**: Q-network and optimisation
- **Pygame**: game logic and rendering
- **Matplotlib**: plotting

<!-- VERIFY: Python version and the exact dependency list -->

## Getting Started

```bash
git clone https://github.com/JHDng/ML_Snake.git
cd ML_Snake
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
pip install torch pygame numpy matplotlib
python agent.py
```

## Implementation Details

**Environment.** Grid-based board; the snake moves cell by cell and the episode ends on collision.
<!-- VERIFY: state representation (which features) and action space (4 absolute directions vs. 3 relative: straight/left/right) -->

**Agent.** A neural network approximates Q(s, a). Actions are chosen ε-greedily, with ε decreasing over games. Transitions (s, a, r, s′, done) are stored in a replay memory and sampled for training.

**Training loop.**
1. Reset the environment.
2. Select an action (ε-greedy).
3. Execute it; observe reward r and next state s′.
4. Store the transition in replay memory.
5. Train the network on sampled transitions to minimise the squared error between Q(s, a) and the target r + γ · max<sub>a′</sub> Q(s′, a′) (target = r if the episode ended).
6. Repeat until game over.

**Rewards.** Positive reward for eating food, negative reward for dying.
<!-- VERIFY: reward values and any per-step reward -->

## Results

No quantitative evaluation has been done yet. Training scores can be plotted with `plotter.py`.

## Possible Extensions

- Evaluate systematically: multiple random seeds, mean and variance of scores, ablations (with vs. without experience replay, different ε schedules)
- Double DQN, Dueling networks, Prioritized Experience Replay
- Convolutional network on raw frames instead of hand-crafted features
- Reward shaping (e.g. distance to food)
- Memory-efficient agents, as in *A Memory Efficient Deep Reinforcement Learning Approach For Snake Game Autonomous Agents*

## Acknowledgements

Based on the tutorial [Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake](https://www.youtube.com/watch?v=L8ypSXwyBds).
