print("WELCOME TO BILL CALCULATOR")
total_bill = int(input("your total bill \n"))
total_tip = int(input("tip you want to give 10 or 20 or 30 :-\n"))
full_total = total_bill + total_tip
print(f"total bill with tip is : - {full_total}")
total_members = int(input("how many members you are there"))
each_person = full_total / total_members
print(f"EACH PERSON SHOULD PAY :- {each_person}")
