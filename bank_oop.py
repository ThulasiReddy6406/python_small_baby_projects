class Account:

    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    def show (self):
        print(f"{self.account_no}--->{self.balance}")

    def debit(self,amount):
        self.balance+=amount
        print(f"RUPEES ${amount} WAS DEBITED")
        print(f"{self.account_no}--->{self.balance}")
    
    def credit(self,amount):
        self.balance-=amount
        print(f"RUPEES ${amount} WAS credited")
        print(f"{self.account_no}--->{self.balance}")

    def bala(self):
        print(f"{self.account_no}--->{self.balance}")

ac_1 = Account(20000,6406)
ac_1.debit(1000)
while True:
    com = input("ANY MORE OPERATIONS :-  ").lower()
    if com =="yes":
        continue
    else:
        break

    
    
    


