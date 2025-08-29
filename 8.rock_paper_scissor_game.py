rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissor = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

game_images = [rock,paper,scissor]
import random

choices = ["rock","paper","scissor"]

player_choice = input("enter your choice :- ")

computer_choice = random.choice(choices)


print(f" computer_choice is :- {computer_choice}")

print(f"Player's choice:\n{game_images[choices.index(player_choice)]}")
print(f"Computer's choice:\n{game_images[choices.index(computer_choice)]}")

if player_choice == computer_choice:
    print("its draw")
elif player_choice == "rock" and computer_choice =="scissor":
    print("BUDDY YOU WON ")
elif player_choice == "scissor" and computer_choice == "paper":
    print("BUDDY YOU WON ")
elif player_choice == "paper" and computer_choice == "rock":
    print("you won buddy!")
else:
    print("comp won !")
