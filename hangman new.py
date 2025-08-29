import random

# ASCII art for Hangman
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word list
word_list = ["apple", "banana", "cat", "dog", "elephant", "frog", "giraffe", "horse", "icecream"]
random_word = random.choice(word_list)

# Game variables
lives = len(HANGMANPICS) - 1
gameover = False
player_guesses = []
word_display = ["_"] * len(random_word)

# Main game loop
while not gameover:
    print(HANGMANPICS[lives])
    print("Word: " + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in player_guesses:
        print("You already guessed that letter.")
    elif guess in random_word:
        player_guesses.append(guess)
        for i, char in enumerate(random_word):
            if char == guess:
                word_display[i] = guess
    else:
        player_guesses.append(guess)
        lives -= 1
        print(f"Incorrect guess! Lives left: {lives}")

    if "_" not in word_display:
        gameover = True
        print("Congratulations! You guessed the word: " + random_word)
    elif lives == 0:
        gameover = True
        print(HANGMANPICS[lives])
        print("Game over! The word was: " + random_word)

print("Thanks for playing!")
