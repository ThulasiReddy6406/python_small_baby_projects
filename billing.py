print("🛒 Welcome to the Billing System!")
print("-------------------------------------")

items = {
    1: ("Chips", 10),
    2: ("Coke", 20),
    3: ("Chocolate Bar", 15),
    4: ("Instant Noodles", 25),
    5: ("Ice Cream Cup", 30),
    6: ("Sandwich", 40),
    7: ("Coffee", 35),
    8: ("Exit", 0)
}
total_bill =0 

for number,(item,price) in items.items():
    print(f"{number} :- {item} :-- {price}")

com = True
while com:

    snack = int(input("ENTER YOU SNACK :-  "))

    if snack == "8":
        print("THANK YOU FOR SHOPING")
    if snack in items:
        item_product , item_price = items[snack]     # DICTIONARIES USED HERE ACCESSING KEY,VALUES IN DICTIONARY
        print(f"product_name=={item_product} and price :- ${item_price}")
        total_bill+=item_price
    other = input("any other items :--  ")
    if other == "yes":
        com = True
    else:
        com = False
        print("TOTAL BILL  $:-",total_bill)