menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}

menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}
go = True
while go:
    choice = input("Choose your choice: espresso/latte/cappuccino ").lower()

    def check_resources(choice):
        for item in menu[choice]:
            if item in resources:
                if resources[item] < menu[choice][item]:
                    print(f"Sorry, there is not enough {item}.")
                    return False
        return True

    if choice in menu:
        if check_resources(choice):
            for item in menu[choice]:
                if item in resources:
                    resources[item] -= menu[choice][item]
            resources["money"] += menu[choice]["cost"]
            print(f"Enjoy your {choice}!")
        else:
            print("Not enough resources to make your drink.")
    else:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")

    print("Remaining resources:", resources)
    
    con = input("yes or no").lower()
    if con == "yes":
        go = True
        
    if con == "no":
        go =False
    

            
    

              
              