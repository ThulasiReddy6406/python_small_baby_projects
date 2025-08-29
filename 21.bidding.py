logo = '''
                         ___________
                                 /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidders = {} 

while True:
    name = input("ENTER YOUR NAME:-  ")
    bid_price = int(input("Enter your bid price:- $"))
    bidders[name] = bid_price  
    next = input("Is there any other bidder? (yes/no): ").lower()
    if next == "yes":
        print("\n" * 100) 
    elif next == "no":
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
    
print("\nAll bids:")
for name, bid in bidders.items():
    print(f"{name}: ${bid}")


highest_bid = 0 
for bi in bidders.values():
    if bi > highest_bid:
        highest_bid = bi

    elif bi < highest_bid:
        highest_bid += 0

    else:
        print("you are wrong!")
print(highest_bid)


for name , bid in bidders.items():
    if str(highest_bid) in str(bid):
        print(f"highest bidder :- {name}  with bid :-  ${bid}")