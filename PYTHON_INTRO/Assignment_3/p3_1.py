import random

# Generate a random number between 1 and 5
random_number2954 = random.randint(1, 5)

# Get user input for guessing the number
guess_expression2954 = input("Guess the number (in expression format): ")

# Evaluate the user's guess
user_guess2954 = eval(guess_expression2954)

# Check if the guess is correct
if user_guess2954 == random_number2954:
    print("Congratulations! You guessed the correct number2954.")
else:
    print(f"Sorry, the correct number2954 was {random_number2954}.")
