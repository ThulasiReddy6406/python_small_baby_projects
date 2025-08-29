# print(''' / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|''')

import random 

print("Welcome to number guessing game ")
print("iam thinking of a number between 1 and 100!")
level = input("choose difficulty type :- 'easy' or 'hard' :--  ").lower()
number = random.randint(1,101)
lifes =0
if level == "easy":
    lifes += 10
elif level =="hard":
    lifes += 5
print(f"you total lifes :- {lifes}")
play = True
while play:
    guess = int(input("Make a guess:- "))
    if guess != number:
        if guess < number:
            print("it is too loo")
            lifes -= 1
        elif guess > number:
            print("you are to high")
            lifes -= 1
        else:
            print(f"you found it the num is {number} ")

    if lifes == 0:
        print("your game is over lifes are completed")
        print(f"The num is {number} ")
        play = False
    elif lifes != 0 :
        print( f"your lifes left {lifes}")
    if guess == number:
        play = False
        print("YOU FIND IT BUDDY")
