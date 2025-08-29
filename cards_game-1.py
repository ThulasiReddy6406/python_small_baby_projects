import random
random_cards =[ 11,1,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards =[]
user_f_card = int(input("TAKE FIRST CARD BUDDY :--  "))
user_s_card = random.choice(random_cards)
 
total = f" {user_f_card},{user_s_card}"
user_cards.append(total)
print(f"OLD_CARDS_BUDDY= {user_cards}")

user_total = user_f_card + user_s_card
print(f"YOUR OLD TOTAL IS : - {user_total}")

print("IF YOU WANT ANOTHER CARD YES IF DONT WANT NO")
extra = input().lower()
if extra == "yes":
    extra_card =random.choice(random_cards)
    user_cards.append(extra_card)
    user_total +=extra_card
    print(f" NEW_CRAD_ADDED :- {user_cards}")
    print(f"USER_NEW_TOTAL =  {user_total}")
elif extra == "no":
    print(f"USER NEW TOTAL=  {user_total}")
    

print("------------------------------------------------------------------------------")

comp =[]
computer_f_card_random = random.choice(random_cards)

computer_s_card_random = random.choice(random_cards)

comp_re = f"COMPUTER_CARDS = {computer_f_card_random} ,{computer_s_card_random} "

comp.append(comp_re)
print(comp)

comp_total = computer_f_card_random + computer_s_card_random
print(f" COMPUTERS TOTAL = {comp_total}")
    
if comp_total < 16:
    extra_one = random.choice(random_cards)
    comp_total+=extra_one
comp.append(extra_one)   
print(f" NEW_CRAD_ADDED :- {comp}")
print(f"COMP_NEW_TOTAL =  {comp_total}")

print("---------------------------------------------------------------------------") 

print(f"USER NEW TOTAL=  {user_total}")
print(f"COMP_NEW_TOTAL =  {comp_total}")

print("----------------------------------------------------------------------")
if comp_total > user_total:
    print(f"COMPUTER WON THE GAME ")
elif comp_total < user_total:
    print(f"BUDDY YOU WON IT ")
else:
    print("ITS DRAW")

