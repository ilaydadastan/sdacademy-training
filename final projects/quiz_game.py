"""
Quiz Game
Problem:
Create a simple quiz game where the user answers multiple-choice questions. The game will keep track of the user's score and show the final result at the end.

Criteria:
Questions & Answers:

The game should present multiple-choice questions to the user.
Each question has three options (A, B, or C), and the user must select the correct one.
Score Tracking:

Keep track of the score and display it at the end of the game.
Award 1 point for each correct answer.
Input Validation:

The user’s answer must be one of the valid options: A, B, or C.
The answer is case-insensitive (i.e., "a" and "A" are both valid).
Game Flow:

The user is presented with each question along with three options.
After answering each question, display whether the answer was correct or not.
At the end of the game, display the total score.

Steps:
Show the list of questions and options to the user.
Get the user’s input and check if it matches the correct answer.
Keep track of the score based on correct answers.
After all questions are answered, display the final score.

"""
def quiz_game():
    # List of questions with possible answers
    questions = [
        {"question": "What is the capital of France?", "options": ["A) Paris", "B) Berlin", "C) Madrid"],
         "correct": "A"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Venus"],
         "correct": "B"},
        {"question": "What is the largest ocean?", "options": ["A) Atlantic", "B) Pacific", "C) Indian"],
         "correct": "B"},
    ]

    score = 0  # Initialize score

    print("Welcome to the Quiz Game!")

    # Loop through each question
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)  # Display options

        # Get user's answer and validate
        answer = input("Enter your answer (A, B, or C): ").upper()

        if answer == question["correct"]:
            print("Correct!")
            score += 1  # Increase score for correct answer
        else:
            print(f"Wrong! The correct answer was {question['correct']}.")

    # Display final score
    print(f"\nGame Over! Your score is {score}/{len(questions)}.")


# Start the quiz
quiz_game()
