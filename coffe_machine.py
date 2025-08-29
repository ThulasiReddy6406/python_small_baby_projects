MENU = {
    "tea": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "coffee": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "latte": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

wel = print("WELCOME TO COFFE MACHINE")

choice = input("WHAT YOU WANT tea or coffee or latte :-  ").lower()

def cheak_resources(choice):
    for items in resources:
        if  items >= MENU[choice]["ingredients"]:
            print(f"enjoy your {choice}")
            MENU[choice]["ingredients"] -= items in resources
        else:
            print("RESOURCES NOT SUFFICIENT ")
total_money = 0
coins = float(input("enter coins of   :- "))
def money(coins):
    if  coins == MENU[choice]["cost"] :
        print(f"enjoy your {choice}")
        MENU[choice]["cost"] += total_money
        print(f"your total money {total_money}")
    else:
        print("you dont have enough money")









