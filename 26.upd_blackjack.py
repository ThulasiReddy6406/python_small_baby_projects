import random
cards =['11','2','3','4','5','6','7','8','7','8','9','10','10','10','10']

game = input("DO YOU WANT TO PLAY BLACKJACK :-  ").lower()
if game == "yes":
    comp_cards = []
    com_fir_card=random.choice(cards)
    comp_sec_card=random.choice(cards)
    comp_cards.append(com_fir_card )
    comp_cards.append(comp_sec_card)
    comp_total = int(com_fir_card)+int(comp_sec_card)
    if comp_total < 16:
        comp_third_card =random.choice(cards)
        comp_cards.append(comp_third_card)
        comp_total = int(com_fir_card)+int(comp_sec_card)+int(comp_third_card)




    user_cards = []
    fir_card=random.choice(cards)
    sec_card=random.choice(cards)
    user_cards.append(fir_card )
    user_cards.append(sec_card)
    total = int(fir_card)+int(sec_card)
    print(f"your cards{user_cards}and its total={total} \n computer first card:- {[com_fir_card]}")
    if total < 16:
        
        take_card = input("do you want to take another card").lower()
        if take_card == "yes":
            third_card = random.choice(cards)
            total = int(fir_card)+int(sec_card)+int(third_card)
            user_cards.append(third_card)

            print(f"your cards{user_cards}and its total={total} \ncomputer card:- {comp_cards} and its total={comp_total}")

        else:
            print(f"your cards{user_cards}and its total={total} \ncomputer card:- {comp_cards} and its total={comp_total}")


    if total== comp_total:
        print("DRAW...")  
    elif total >21:
        print("comp win THE GAME")

    elif comp_total >21:
        print("YOU WIN THE GAME")





    

        




