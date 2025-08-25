# Snake AI with Q-Learning (Python • PyTorch • Pygame)

## Overview

This project demonstrates how to train an AI agent to master the classic Snake game using the Q-learning algorithm. It follows the tutorial “Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake” ([Link to the video](https://www.youtube.com/watch?v=L8ypSXwyBds)).

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
   - [Installation](#installation)  
   - [Usage](#usage)  
4. [Implementation Details](#implementation-details)  
   - [Game Environment](#game-environment)  
   - [Q-Learning Agent](#q-learning-agent)  
   - [Training Loop](#training-loop)  
   - [Rewards & Exploration Strategy](#rewards--exploration-strategy)  
5. [Results & Visuals](#results--visuals)  
6. [How to Extend](#how-to-extend) 
7. [Acknowledgements](#acknowledgements)

---

## Features

- Functional Snake game with movement, growth, collisions  
- Q-learning agent that learns via game-play rewards  
- Configurable parameters: learning rate, discount factor, epsilon (exploration)  
- Real-time visualization with Pygame for training observation

---

## Tech Stack

- **Python 3.7** – base language  
- **PyTorch** – builds and updates Q-function (deep or tabular)  
- **Pygame** – game rendering and mechanics  
- **Optional**: NumPy, Matplotlib (for plotting metrics)

---

## Getting Started

### Installation

```bash
git clone https://github.com/JHDng/ML_Snake.git
cd your_directory
python3 -m venv venv # activate environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
[...] # install dependencies
```

### Usage

```bash
python agent.py
```

## Implementation Details

### Game Environment

- **Grid-based**: The game board is virtually divided into cells; snake moves cell-by-cell.  
- **State Representation**: Typically includes directional information, snake head position, food relative position, and collisions.  
- **Actions**: {Up, Down, Left, Right}.

### Q-Learning Agent

- **State-action value table (Q-table)** or approximated by a neural network.  
- **Parameters**:
  - **α (learning rate)**
  - **γ (discount factor)**
  - **ε (exploration probability)** with decay over games.

### Training Loop

1. Reset environment.  
2. Agent selects action (ε-greedy policy).  
3. Execute action, observe reward and next state.  
4. Update Q(s,a): Q(s,a) ← Q(s,a) + α [ r + γ max_a' Q(s',a') - Q(s,a) ]
5. Decay ε. 
6. Repeat until game over or limit reached.

### Rewards & Exploration Strategy

- **Positive reward** for eating food.  
- **Negative or small penalty** for collisions or non-progress moves.  
- Encouragement for survival via tiny positive reward per time step can improve learning stability.

---

## Results & Visuals

- Early training: agent moves randomly, loses quickly.  
- Mid-training: learns to approach food, avoid walls.  
- Late-training: reliably collects food, grows long.

---

## How to Extend

- Switch from tabular Q-learning to **Deep Q-Network (DQN)** using neural networks.  
- Apply **Double Q-learning**, **Dueling networks**, or **Prioritized Experience Replay** for stability.  
- Use **convolutional layers** (CNNs) for pixel-based input (screen frames).  
- Experiment with **reward shaping** (e.g., survival reward, distance to food).  
- Optimize performance: smaller memory usage, faster learning—similar to research like “A Memory Efficient Deep Reinforcement Learning Approach For Snake Game Autonomous Agents”

---

## Acknowledgements

- Based on **Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake** tutorial ([Link to the video](https://www.youtube.com/watch?v=L8ypSXwyBds)).  
- Inspiration from classical Q-learning literature and reinforcement learning fundamentals.
