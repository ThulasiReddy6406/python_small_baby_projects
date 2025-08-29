print("Welcome to the Pizza Delivery App! 🍕")

# Taking user inputs
size = input("Which size of pizza do you want? (S/M/L): ").lower()
peppor = input("Do you want pepperoni? (Y/N): ").lower()
cheese = input("Do you want extra cheese? (Y/N): ").lower()

# Initialize bill
bill = 0

# Pricing for size
if size == "s":
    bill += 10
    print("Your small-size pizza costs: $10")
elif size == "m":
    bill += 20
    print("Your medium-size pizza costs: $20")
elif size == "l":
    bill += 30
    print("Your large-size pizza costs: $30")
else:
    print("Invalid size selected! Exiting...")
    exit()
if peppor == "y":
    bill +=5
    print("Pepperoni added: +$5")

if cheese == "y":
    bill += 5
    print("Extra cheese added: +$5")

print(f"Your total bill: **${bill}**. Enjoy your pizza! 🍕")
# Final bill


# Adding extra toppings


        