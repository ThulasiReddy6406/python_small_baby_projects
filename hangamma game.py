HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


import random
lives =  6
word_list = [ "reddy", "nanii","jashuu"]
any_random_one = random.choice(word_list)
print(any_random_one)

placeholder = ""
wordlen = len(any_random_one)
for position in range(wordlen):
    placeholder += "-"
print(placeholder)

gameover = False

correctletters = []
while not gameover:
    guess_letter = input("guess a letter in word").lower()

    display = ""
    
    for char in any_random_one:
        if char == guess_letter:
            display+=char
            correctletters.append(char)
        elif char in correctletters:
            display += char
        else:
            display+="-"
        
    print(display)
    
    if  guess_letter not in any_random_one:
        if lives == 0:
            print("gameover")

    if "-" not in display:
        gameover = True
        print("you win")

    print(HANGMANPICS[lives])   