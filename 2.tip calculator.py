print("WELCOME TO TIP CALCULATOR")
total_bill = int(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split_bill = int(input("How many people to split the bill?"))

total = (total_bill + tip)/split_bill
print(f"each person should pay \n ${total} rupees" )
