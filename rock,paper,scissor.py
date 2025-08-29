import random

print("WELCOME TO  \"ROCK\"  \"PAPER\"  \"SCISSOR\"")

COMPUTER_CHOICE =["rock" , "paper" , "scissor" ]
computer_final_choice = random.choice(COMPUTER_CHOICE)

user_input = input("enter your choice \"rock\" \"paper\"  \"scissor\"")

if user_input == "rock" and computer_final_choice == "rock":
    print("THE GAME IS DRAW")
  
elif user_input == "paper" and computer_final_choice == "paper":
    print("THE GAME IS DRAW")
    
elif user_input == "scissor" and computer_final_choice == "scissor":
    print("THE GAME IS DRAW")
    
elif user_input == "paper" and computer_final_choice == "rock":
    print("COMPUTER WON THE GAME")
    
elif user_input == "paper" and computer_final_choice == "rock":
    print("COMPUTER WON THE GAME")
    
elif user_input == "paper" and computer_final_choice == "scissor":
    print("COMPUTER WON THE GAME")

elif user_input == "scissor" and computer_final_choice == "paper":
    print("YOU WON THE GAME")
    
elif user_input == "scissor" and computer_final_choice == "ROCK":
    print("COMP WON THE GAME")

elif user_input == "rock" and computer_final_choice == "scissor":
    print("YOU WON THE GAME")
    
else:
    print("enter a valid answer")
    
print(computer_final_choice)
