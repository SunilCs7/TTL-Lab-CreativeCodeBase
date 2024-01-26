import random

# Generate and display ten multiplication questions
for i in range(1, 11):
    num1_2954 = random.randint(1, 10)
    num2_2954 = random.randint(1, 10)

    # Get user input for the answer
    user_answer2954 = int(input(f"Question {i}: {num1_2954} x {num2_2954} = "))

    # Check if the answer is correct
    if user_answer2954 == num1_2954 * num2_2954:
        print("Right!2954")
    else:
        print(f"Wrong. The correct answer2954 is {num1_2954 * num2_2954}.")
