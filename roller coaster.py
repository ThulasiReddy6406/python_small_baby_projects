print("WELCOME TO ROLLER COASTER")

height = int(input("enter your height :-"))
bill = 0

if height > 120 :
    print("you can ride")
    age = int(input("your age "))
    if age < 12:
        bill +=20
        print("you have to pay $ 20")
        
    elif age > 12 and age < 18:
        bill+=70
        print("you have to pay $70")
        
    else:
        bill += 20
        print("it is $12")
        
        photo = input("if you want photos yes or no ")
        
    if photo == "yes":
        bill += 100
        print("it costs $100 rupees")
        print(f"total balance {bill}")
    else:
        print(f"your total bill is {bill}")
            
else:
    print("you cant ride")