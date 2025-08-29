sbi_bank_holders = [("RAKSHITHA ISHWAR PATEL", 123456, 45000),
                    ("THULASI REDDY", 64069820, 100000),
                    ("MOHIT PATEL", 9820, 50000),
                    ("SUNITHA PATEL", 2344, 56000),
                    ("ISHWAR PATEL", 4567, 90000),
                    ("JAY KOTHAWADE", 112233, 13000),
                    ("DUCCAR", 6406, 21000)]

print("WELCOME TO SBI ATM")
pin = int(input("PLEASE LOGIN INTO SBI BANK WITH YOUR PIN: "))
conti = True
while conti:

    def login(pin):
        for details in sbi_bank_holders:
            if details[1] == pin:
                print(f"LOGIN SUCCESSFUL !!!! WELCOME ------> {details[0]} <------- TO SBI BANK !!!")
                return details  
        print("INVALID PIN! Please try again.")  
        return None

    user = login(pin)

    if user:
        menu = input("SIR/MAM, WHAT CHANGES DO YOU WANT TO DO? 1.DEPOSIT 2.WITHDRAW 3.CHECK BALANCE: ").lower()

        if menu == "deposit":
            money = float(input("HOW MUCH MONEY DO YOU WANT TO DEPOSIT? "))

            def deposit(money):
                global sbi_bank_holders 
                updated_sbi_bank_list = []

                for details in sbi_bank_holders:
                    if details[1] == user[1]:  
                        update_list = (details[0], details[1], details[2] + money)
                        updated_sbi_bank_list.append(update_list)
                        print(f"MONEY SUCCESSFULLY DEPOSITED! TOTAL BALANCE: {update_list[2]}")  
                    else:
                        updated_sbi_bank_list.append(details)

                sbi_bank_holders = updated_sbi_bank_list  

            deposit(money)
        if menu == "withdraw":
                money_ = float(input("HOW MUCH MONEY DO YOU WANT TO WITHDRAW? "))
                def withdrwa(money_):
                    global sbi_bank_holders 
                    updated_sbi_bank_list = []

                    for details in sbi_bank_holders:
                        if details[1] == user[1]:  
                            update_list = (details[0], details[1], details[2] - money_)
                            updated_sbi_bank_list.append(update_list)
                            print(f"MONEY SUCCESSFULLY WITHDRAWED! TOTAL BALANCE: {update_list[2]}")  
                        else:
                            updated_sbi_bank_list.append(details)

                    sbi_bank_holders = updated_sbi_bank_list  
                withdrwa(money_)
        if menu == "cheakbalance":
            for details in sbi_bank_holders:
                if details[1]==user[1]:
                    print(f"YOUR CURRENT BALANCE IS {details[2]}")
    con = input("ANY OTHER TRANSACTIONS LEFT :-  ").lower()
    if con == "yes":
        conti = True
    if con == "no":
        print("-------------> THANK YOU FOR VISITING <-------------------")
        break
    else:
        print("-------------> THANK YOU FOR VISITING <-------------------")
    
