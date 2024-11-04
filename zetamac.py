import time
import random
import operator
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }
    operation = random.choice(list(operations.keys()))
    if operation == "/":
        num1 *= num2
    question = f"{num1} {operation} {num2} = ?"
    answer = operations[operation](num1, num2)
    return question, answer

def start_game():
    duration = 200
    start_time = time.time()
    score = 0

    print("\nGame Started! Answer as many math questions as you can in 200 seconds.")
    
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration - int(elapsed_time)

        if remaining_time <= 0:
            print(f"\nGame Over! Time is up.\nYour final score is: {score}")
            break

        question, correct_answer = generate_question()
        
        while True:
            clear_screen()
            print(f"Time remaining: {remaining_time} seconds | Score: {score}")
            print(question)

            try:
                user_answer = int(input("Your answer: "))
                if user_answer == correct_answer:
                    print("Correct!\n")
                    score += 1
                    break
                else:
                    print("Wrong! Try again.")
            
            except ValueError:
                print("Invalid input. Please enter an integer.\n")

            elapsed_time = time.time() - start_time
            remaining_time = duration - int(elapsed_time)
            if remaining_time <= 0:
                print(f"\nGame Over! Time is up.\nYour final score is: {score}")
                return

if __name__ == "__main__":
    start_game()
