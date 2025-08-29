import random

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
comp_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

play = True

while play:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {comp_cards[0]}")
    
    if user_score == 0 or comp_score == 0 or user_score > 21:
        play = False
    else:
        should_continue = input("Type 'y' to get another card, 'n' to pass: ")
        if should_continue == 'y':
            user_cards.append(deal_card())
        else:
            play = False

# Computer plays its turn
while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")

if user_score > 21:
    print("You went over. You lose!")
elif comp_score > 21 or user_score > comp_score:
    print("You win!")
elif user_score == comp_score:
    print("It's a draw!")
else:
    print("You lose!")

    
    
    
    
    
    