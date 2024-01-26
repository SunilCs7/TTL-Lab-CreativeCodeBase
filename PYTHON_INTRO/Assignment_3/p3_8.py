import random

def determine_winner2954(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win2954!"
    else:
        return "Computer wins2954!"

# Play Rock-Paper-Scissors for five rounds
for round2954 in range(1, 6):
    print(f"\nRound {round2954}:")
    
    # Get user choice
    user_choice2954 = input("Enter your choice (rock, paper, scissors): ").lower()

    # Get computer choice
    computer_choice2954 = random.choice(["rock", "paper", "scissors"])

    print(f"Computer's choice: {computer_choice2954}")
    print(determine_winner2954(user_choice2954, computer_choice2954))

print("\nGame Over2954!")
