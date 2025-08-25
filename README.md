# Snake AI with Q-Learning (Python • PyTorch • Pygame)

## Overview

This project demonstrates how to train an AI agent to master the classic Snake game using the Q-learning algorithm. It follows the tutorial “Python + PyTorch + Pygame Reinforcement Learning – Train an AI to Play Snake” ([youtube.com](https://www.youtube.com/watch?v=L8ypSXwyBds)).

You’ll learn:
- How to build the Snake game environment using Pygame  
- Design and logic behind Q-learning (tabular or deep)  
- Integration of Python, PyTorch, and Pygame  
- Training the AI to improve gameplay over time

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
6. [Evaluation & Metrics](#evaluation--metrics)  
7. [How to Extend](#how-to-extend)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)

---

## Features

- Functional Snake game with movement, growth, collisions  
- Q-learning agent that learns via game-play rewards  
- Configurable parameters: learning rate, discount factor, epsilon (exploration)  
- Real-time visualization with Pygame for training observation

---

## Tech Stack

- **Python 3.10+** – base language  
- **PyTorch** – builds and updates Q-function (deep or tabular)  
- **Pygame** – game rendering and mechanics  
- **Optional**: NumPy, Matplotlib (for plotting metrics)

---

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/snake-qlearning.git
cd snake-qlearning
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
