import time
import random
import operator
import os
import threading

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

def display_timer(duration, start_time, stop_event):
    while not stop_event.is_set():
        elapsed_time = time.time() - start_time
        remaining_time = duration - int(elapsed_time)
        if remaining_time <= 0:
            print("\nTime's up!")
            stop_event.set()
            break
        print(f"\rTime remaining: {remaining_time} seconds", end="")
        time.sleep(1)

def start_game():
    duration = 200
    start_time = time.time()
    score = 0
    stop_event = threading.Event()

    timer_thread = threading.Thread(target=display_timer, args=(duration, start_time, stop_event))
    timer_thread.start()

    print("\nGame Started! Answer as many math questions as you can in 200 seconds.")
    
    while not stop_event.is_set():
        question, correct_answer = generate_question()
        
        while True:
            clear_screen()
            elapsed_time = time.time() - start_time
            remaining_time = duration - int(elapsed_time)
            if remaining_time <= 0:
                stop_event.set()
                break

            print(f"Score: {score}")
            print(f"\nTime remaining: {remaining_time} seconds | Question: {question}")

            try:
                user_answer = int(input("Your answer: "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("Wrong! Try again.")
            
            except ValueError:
                print("Invalid input. Please enter an integer.\n")

    stop_event.set()
    timer_thread.join()
    print(f"\nGame Over! Your final score is: {score}")

if __name__ == "__main__":
    start_game()
