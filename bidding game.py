



bids = {}
continue_bidding = True
while continue_bidding:
       
       
       name = input("enter your name")
        prize = int(input("enter your amount"))
    
      
      bids[name] = prize
        shall_con = input("continnue or not ").lower()
        if shall_con == "no":
            continue_bidding = False
            
        
        elif shall_con == "yes":
            continue_bidding = True
        
def compare_bids(bidding_book):
     winner = ""
     highest_bid = 0
     for bidder in bidding_book:
         amount = bidding_book[bidder]
         if amount > highest_bid :
             highest_bid = amount
             winner = bidder
            
     print(f"winner is {winner} with bid of {highest_bid}")
        



compare_bids(bids)       

