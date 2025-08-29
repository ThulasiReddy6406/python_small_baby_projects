import random
cards =['1','2','3','4','5','6','7','8','7','8','9','10','11','12','13']

play_bold = True
while play_bold:
    play = input("Do you want to play blackjack game  'y' or 'n' ").lower()
    # if play == "y":

        # print('''
        #         ------              _     _            _    _            _    
        #         |A_  _ |.          | |   | |          | |  (_)          | |   
        #         |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        #         | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
        #         |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        #         '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
        #             |  \/ K|                            _/ |                
        #             '------'                           |__/ ''')

    your_cards = []
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    sum_ = int(first_card)+ int(second_card)
    your_cards.append(sum_)
    print(f"your cards{first_card,second_card}total of{[sum_]}")

    for num in first_card or second_card:
        if num=="10":
            print("you have blackjack")

    extra_card = input("do you want another card 'y' or 'n' " ).lower()
    if extra_card == "y":
        third_card=random.choice(cards)
        sum_+=int(third_card)
        print(f"your cards{first_card,second_card,third_card}total of{[sum_]}")

    else:
        print(f"your cards{first_card,second_card}total of{[sum_]}")


    comp_cards = []
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    comp_sum = int(first_card)+ int(second_card)
    comp_cards.append(comp_sum)
    print(f"comp cards{first_card,second_card}total of{[comp_sum]}")

    for num in first_card or second_card:
        if num=="10":
            print("comp have blackjack")


    if comp_sum < sum_:
        third_card=random.choice(cards)
        comp_sum+=int(third_card)
        print(f"comp cards{first_card,second_card,third_card}total of{[comp_sum]}")

    else:
        print()


    if sum_ > comp_sum:
        print("you win buddy")

    elif comp_sum > sum_:
        print("computer win ")

    else:
        print("finish")

    want_to_play = input("do you want to play 'y' or 'n' " ).lower()

    if want_to_play == "y":
        play_bold = True

    elif want_to_play == "n":
        play_bold = False

    else:
        print("choose corecct option")

        
