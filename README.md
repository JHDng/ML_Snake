# 🐍 Snake AI with Q-Learning & PyTorch  

This repository contains a **Machine Learning project** that teaches an agent to play the classic **Snake Game** using **Q-Learning**, **Deep Q-Networks (DQN)**, and **PyTorch**. The project demonstrates how reinforcement learning can be applied to a simple game environment, and it provides modular implementations of the game logic, agents, and training pipeline.  

---

## 📌 Project Overview  

The goal of this project is to train an **AI agent** that can successfully play Snake by learning optimal policies through trial and error.  
The agent uses **reinforcement learning** to maximize cumulative rewards while avoiding collisions and collecting food.  

**Key aspects:**  
- ✅ **Custom Snake game environment** built in Python.  
- ✅ **Q-Learning agent** for tabular reinforcement learning.  
- ✅ **Deep Q-Learning agent (DQN)** implemented in **PyTorch**.  
- ✅ Modular design with game logic, agents, and training separated.  
- ✅ Training visualization and performance tracking (scores, plots).  

---

## 🎮 Game Environment  

The Snake game is implemented from scratch using **Python (Pygame/graphics or CLI, depending on your implementation)**.  
It defines the state space and reward function used by the agents:  

### 🔹 State Representation  
- Danger (left, right, straight)  
- Current direction  
- Food position (relative to snake head)  
- Snake length  

### 🔹 Actions  
- `Straight`  
- `Left turn`  
- `Right turn`  

### 🔹 Reward Function  
- `+10` for eating food  
- `-10` for dying  
- `0` for each step (or small penalty for survival incentive tweaking)  

---

## 🧠 Agents  

### 🔹 Q-Learning Agent  
- Uses a **Q-Table** to store `(state, action)` values.  
- Learns via **Bellman equation**:
- Q(s, a) ← Q(s, a) + α [r + γ max(Q(s’, a’)) – Q(s, a)]

- - Works well on smaller state spaces, but suffers from scalability issues.  

### 🔹 Deep Q-Network (DQN) Agent  
- Uses a **Neural Network** (PyTorch) to approximate Q-values.  
- **Architecture**:  
- Input: Encoded state vector.  
- Hidden layers: Fully connected layers with ReLU activation.  
- Output: Q-values for each possible action.  
- **Techniques implemented**:  
- Experience Replay (Replay Buffer).  
- ε-greedy policy for exploration vs. exploitation.  
- Discounted future rewards (γ).  
- Target network updates (optional, if implemented).  

---

## 📂 Project Structure  

📦 snake-rl
┣ 📜 README.md
┣ 📜 requirements.txt
┣ 📜 train.py # Training loop
┣ 📜 play.py # Run a trained agent
┣ 📂 game
[PLACEHOLDER]

---

## 🚀 Getting Started  

### 1️⃣ Clone Repository  

git clone https://github.com/your-username/snake-rl.git
cd snake-rl
2️⃣ Install Dependencies
pip install -r requirements.txt


Dependencies:

torch – Deep learning framework.

pygame – Snake game environment.

numpy, matplotlib – Data handling & visualization.

3️⃣ Train an Agent
python train.py --agent dqn --episodes 1000


Options:

--agent [q|dqn] → Choose Q-Learning or DQN.

--episodes N → Number of training episodes.

--render → Show game window during training (slows down training).

4️⃣ Play with a Trained Agent
python play.py --model results/checkpoint.pth

📊 Results

During training, the agent’s performance is tracked with:

Average score per episode.

Moving average of last N episodes.

Exploration rate (ε) over time.

Example training curve:

🛠️ Future Improvements

Implement Double DQN to reduce overestimation bias.

Add Dueling DQN architecture for better stability.

Try Prioritized Experience Replay.

Experiment with different reward functions.

Train on larger board sizes and more complex variations.

📖 References

Sutton & Barto, Reinforcement Learning: An Introduction

DeepMind’s DQN paper (2015): Playing Atari with Deep Reinforcement Learning

PyTorch documentation: https://pytorch.org

🤝 Contributing

Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.
