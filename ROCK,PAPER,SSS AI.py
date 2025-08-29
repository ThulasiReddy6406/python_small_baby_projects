import random

print('WELCOME TO "ROCK" "PAPER" "SCISSOR"')
import random

print('WELCOME TO "ROCK" "PAPER" "SCISSOR"')

# Choices
COMPUTER_CHOICES = ["rock", "paper", "scissor"]
computer_final_choice = random.choice(COMPUTER_CHOICES)

# User input
user_input = input('Enter your choice ("rock", "paper", "scissor"): ').lower()

# Check if input is valid
if user_input not in COMPUTER_CHOICES:
    print("❌ Invalid choice! Please choose 'rock', 'paper', or 'scissor'.")
else:
    print(f"Computer chose: {computer_final_choice}")

    # Check for a draw
    if user_input == computer_final_choice:
        print("🤝 THE GAME IS A DRAW!")
    
    # Winning conditions for the user
    elif (user_input == "rock" and computer_final_choice == "scissor") or \
         (user_input == "paper" and computer_final_choice == "rock") or \
         (user_input == "scissor" and computer_final_choice == "paper"):
        print("🎉 YOU WON THE GAME!")
    
    # If it's not a draw and the user didn't win, the computer wins
    else:
        print("💻 COMPUTER WON THE GAME!")

