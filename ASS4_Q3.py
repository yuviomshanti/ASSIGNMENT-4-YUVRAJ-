import random

print("Welcome to the multiplication game!")
print("You will get 10 questions to answer. Let's begin!")

score = 0

for i in range(1, 11):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    user_answer = int(input(f"Question {i}: {num1} x {num2} = "))

    if user_answer == answer:
        print("Right!")
        score += 1
    else:
        print(f"Wrong. The answer is {answer}.")

print(f"Game Over! Your score is {score} out of 10.")
