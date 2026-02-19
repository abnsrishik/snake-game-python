# 🐍 Snake Game – Object-Oriented Python Implementation

## 📌 Project Overview

This project is a **classic Snake Game** built using Python’s `turtle` graphics module.

The game features:

* Real-time movement
* Keyboard-controlled direction changes
* Collision detection (food, wall, tail)
* Dynamic score tracking
* Modular, object-oriented design

This project demonstrates structured software design using classes and multiple files.

---

## 🎯 Why This Project?

I built this project to strengthen my understanding of:

* Object-Oriented Programming (OOP)
* Class-based architecture
* Event-driven programming
* Real-time game loops
* Collision detection logic

Unlike simple scripts, this project separates responsibilities into multiple classes, improving scalability and maintainability.

---

## 🧠 Core Concepts Used

* Object-Oriented Programming
* Class inheritance
* Event listeners (`onkey`)
* Real-time screen updates
* Collision detection using distance checks
* Game state management
* Modular project organization
* Animation control using `tracer()` and `update()`

---

## 🗂️ Project Structure

```
snake-game-python/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
└── README.md
```

---

### 🔹 `main.py`

* Initializes the game screen
* Controls the main game loop
* Handles collision detection
* Manages game state transitions 

---

### 🔹 `snake.py`

* Defines the `Snake` class
* Controls movement logic
* Manages body segments
* Handles direction control 

---

### 🔹 `food.py`

* Defines the `Food` class
* Randomizes food placement
* Handles food refresh logic 

---

### 🔹 `scoreboard.py`

* Tracks player score
* Updates display dynamically
* Displays “Game Over” state 

---

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/snake-game-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd snake-game-python
   ```

3. Run the game:

   ```bash
   python main.py
   ```

No external libraries are required. The game uses Python’s built-in `turtle` module.

---

## 🎮 Game Mechanics

* Use arrow keys to control the snake.
* Eat blue food to increase score.
* Avoid:

  * Hitting the wall
  * Colliding with your own tail

The game ends when a collision occurs.

---

## 🎓 Learning Outcomes

Through this project, I developed:

* Stronger understanding of OOP design
* Experience with modular file structure
* Knowledge of animation timing and rendering
* Practical experience with collision detection
* Ability to manage dynamic state in interactive systems

---

## 🚀 Future Improvements

* Add high score persistence
* Add restart functionality
* Add difficulty levels (speed increase)
* Add sound effects
* Implement pause functionality
* Convert into a graphical UI-based game

---

## 👤 Author

**A.B.N.S Rishik**

First-Year B.Tech (Artificial Intelligence) Student

SRM Institute of Science and Technology, Ramapuram Campus

📍 Chennai, India

✉️ Email: [rishikcr72401@gmail.com](mailto:rishikcr72401@gmail.com)

🔗 LinkedIn: [https://www.linkedin.com/in/abnsrishik](https://www.linkedin.com/in/abnsrishik)

---

⭐ *Developing structured, object-oriented systems as a foundation for advanced AI and software engineering.*


