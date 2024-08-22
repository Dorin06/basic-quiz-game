# Simple Quiz Game

# Function to ask a question and get user's answer
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if answer in range(1, 5):  # Ensures the answer is within valid range
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if options[answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}\n")
        return False

# Function to run the quiz
def run_quiz():
    # Define the quiz questions, options, and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Mars", "Venus"],
            "answer": "Jupiter"
        },
        {
            "question": "What is the boiling point of water?",
            "options": ["90°C", "100°C", "80°C", "120°C"],
            "answer": "100°C"
        }
    ]
    
    score = 0
    
    # Loop through each question
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1
    
    # Final feedback and score display
    print(f"Quiz finished! Your final score is {score} out of {len(questions)}.")
    
    # Additional feedback based on score
    if score == len(questions):
        print("Excellent! You got all questions right!")
    elif score >= len(questions) // 2:
        print("Good job! You did well!")
    else:
        print("Better luck next time!")

# Entry point of the program
if __name__ == "__main__":
    run_quiz()
