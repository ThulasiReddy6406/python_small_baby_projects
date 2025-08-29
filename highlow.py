import random

# Data of popular people/accounts
data = [
    {"name": "Instagram", "follower_count": 650},
    {"name": "Cristiano Ronaldo", "follower_count": 600},
    {"name": "Ariana Grande", "follower_count": 380},
    {"name": "Dwayne Johnson", "follower_count": 390},
    {"name": "Selena Gomez", "follower_count": 420},
    {"name": "Kylie Jenner", "follower_count": 450},
    {"name": "Lionel Messi", "follower_count": 470},
    {"name": "Kim Kardashian", "follower_count": 360},
    {"name": "Beyoncé", "follower_count": 320},
    {"name": "Neymar", "follower_count": 310}
]

score = 0
game_on = True

# Start with one random account
account_a = random.choice(data)

while game_on:
    # Choose a different account for comparison
    account_b = random.choice(data)
    while account_b == account_a:
        account_b = random.choice(data)

    print(f"\nA: {account_a['name']} with {account_a['follower_count']}M followers")
    print(f"B: {account_b['name']} with {account_b['follower_count']}M followers")

    # Ask the user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if the guess is correct
    if (guess == "A" and account_a['follower_count'] > account_b['follower_count']) or \
       (guess == "B" and account_b['follower_count'] > account_a['follower_count']):
        score += 1
        print(f"Correct! 🎉 Your score is: {score}")
        # Continue the game with the winner as the next A
        account_a = account_a if guess == "A" else account_b
    else:
        print(f"Wrong! ❌ Final score: {score}")
        game_on = False
