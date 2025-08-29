import random

data = [
    {"name": "Instagram", "followers": 500_000_000},
    {"name": "Facebook", "followers": 2_900_000_000},
    {"name": "Twitter", "followers": 330_000_000},
    {"name": "TikTok", "followers": 1_500_000_000},
    {"name": "YouTube", "followers": 2_000_000_000},
    {"name": "Justin Bieber", "followers": 170_000_000},
    {"name": "Cristiano Ronaldo", "followers": 250_000_000},
    {"name": "Beyoncé", "followers": 150_000_000},
    {"name": "NASA", "followers": 70_000_000},
    {"name": "National Geographic", "followers": 200_000_000},
    {"name": "Kylie Jenner", "followers": 280_000_000},
    {"name": "Kim Kardashian", "followers": 270_000_000},
    {"name": "Ariana Grande", "followers": 240_000_000},
    {"name": "Google", "followers": 1_800_000_000},
    {"name": "Amazon", "followers": 800_000_000},
]

def play_game(data):
    score = 0
    correct = True
    a = random.choice(data)
    b = random.choice(data)
    
    while correct:
        a = b
        b = random.choice(data)
        
        if  a == b:
            b = random.choice(data)
        
        print(f"Compare A: {a['name']} ")
        print("vs")
        print(f"Compare B: {b['name']}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (guess == "a" and a["followers"] > b["followers"]) or \
           (guess == "b" and b["followers"] > a["followers"]):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            correct = False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game(data)










