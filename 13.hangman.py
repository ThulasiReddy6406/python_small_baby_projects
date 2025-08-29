HANGMAN_PICS = [
    """
         +====++
         |    ||
              ||
              ||
              ||
              ||
        ______||
    """,
    """
         +====++
         |    ||
         O    ||
              ||
              ||
              ||
        ______||
    """,
    """
         +====++
         |    ||
         O    ||
         |    ||
              ||
              ||
        ______||
    """,
    """
         +====++
         |    ||
         O    ||
        /|    ||
              ||
              ||
        ______||
    """,
    """
         +====++
         |    ||
         O    ||
        /|\\   ||
              ||
              ||
        ______||
    """,
    """
         +====++
         |    ||
         O    ||
        /|\\   ||
         |    ||
              ||
        ______||
    """
]



# print(
# '''  
                                               
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/
# ''' 
# )

from logging import PlaceHolder
from pickle import TRUE
import random
from tkinter import YES


# Word list
words = [
    "Aspect", "Breeze", "Cactus", "Desert", "Forest", "Garden",
    "Hockey", "Island", "Jumper", "Knight", "Lantern", "Monkey",
    "Orbit", "Pencil", "Rocket", "Season", "Temple", "Uniquely",
    "Vision", "Winter"
]

# Choose a random word
random_word = random.choice(words)
# print(random_word)
placeholder = "-" * len(random_word)
correct_letters = set()
lifes = 6

print(f"Word to guess: {placeholder}")

while lifes > 0:
    display = ""
    guess = input("Guess a letter (1st letter is capital): ")
    
    if guess in random_word:
        correct_letters.add(guess)
    else:
        lifes -= 1
        print(f"Incorrect! You have {HANGMAN_PICS[lifes]} lives left.")
        print(f"Incorrect! You have {lifes} lives left.")
    
    # Build display string
    for letter in random_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "-"
    
    print(f"Current word: {display}")
    
    if "-" not in display:
        print("You win!")
        break
else:
    print(f"You lost! The word was: {random_word}")
