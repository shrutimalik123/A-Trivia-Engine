def run_quiz():
    # 1. Setup the Questions
    # Each question is a dictionary containing the prompt, options, and correct answer
    questions = [
        {
            "prompt": "What is the correct file extension for Python files?",
            "options": ["A. .pyt", "B. .py", "C. .pt", "D. .exe"],
            "answer": "B"
        },
        {
            "prompt": "Which keyword is used to create a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "prompt": "How do you insert COMMENTS in Python code?",
            "options": ["A. //", "B. #", "C. ", "D. /*"],
            "answer": "B"
        }
    ]

    score = 0

    print("--- 🧠 Python Beginner Quiz 🧠 ---")
    print("Type the letter of your answer (A, B, C, or D).\n")

    # 2. Game Loop
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['prompt']}")
        for option in q['options']:
            print(option)
        
        # Get user input
        guess = input("Your answer: ").strip().upper()

        # 3. Check the answer
        if guess == q['answer']:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")
        print("-" * 30)

    # 4. Final Result
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print(f"\nQuiz Finished!")
    print(f"Your Score: {score}/{total_questions} ({percentage}%)")

    if percentage == 100:
        print("🏆 Perfect Score! You're a Python pro!")
    elif percentage >= 50:
        print("👍 Good job! You know your basics.")
    else:
        print("📚 Keep practicing! You'll get it.")

# Run the game
run_quiz()
