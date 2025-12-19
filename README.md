# 🧠 Python Trivia Engine - A Simple Quiz Game

This is a flexible, text-based quiz application built in Python. It allows users to answer multiple-choice questions, tracks their score in real-time, and provides a final grade and feedback based on performance.

This project is designed to help beginners master:
* **Complex Data Structures:** Managing a list of dictionaries.
* **Iteration:** Using `for` loops to process a collection of data.
* **Input Cleaning:** Using string methods to make the program "smarter" and more forgiving.
* **Basic Math:** Calculating percentages and final scores.

---

## ✨ Features

* **Multiple Choice Format:** Clear A, B, C, or D options for every question.
* **Smart Input:** Automatically handles lowercase answers and accidental spaces.
* **Instant Feedback:** Tells the player immediately if they got the answer right or wrong.
* **Dynamic Scoring:** Calculates a percentage score and provides a personalized message at the end.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed. No extra libraries are required.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `quiz.py`.
2.  **Open Terminal:** Open your command prompt or terminal.
3.  **Run the Script:**
    ```bash
    python quiz.py
    ```

### 3. Gameplay
1. Read the question and the four options provided.
2. Type the letter of your choice and press **Enter**.
3. At the end of the quiz, review your final score and percentage.

---

## 🧠 Code Structure Highlights

### Data Storage
The game uses a **List of Dictionaries**. This structure is highly scalable—you can add 100 more questions just by adding new dictionaries to the list without changing a single line of the actual game logic.


### The Loop Engine
The `for` loop iterates through the list. We use `enumerate()` to keep track of the question number automatically.

```python
for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['prompt']}")
    # logic to get answer and check it...
