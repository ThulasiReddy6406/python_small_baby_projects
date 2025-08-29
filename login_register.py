# print("!!!------->WELCOME TO 1X BETTING APP <-------------- !!!")

# bet_database = []

# user_name = input("ENTER YOUR USER NAME :-  ")
# password = input("ENTER YOUR PASSWORD :-  ")

# if (user_name ,password )not in bet_database:
#     bet_database.append((user_name , password))
#     print("✅ Registered successfully! You are now logged in.")
# else:
#     print("LOGIN SUCCESFULLY")


print("!!!-------> WELCOME TO 1X BETTING APP <-------------- !!!")



bet_database = []

user_name = input("ENTER YOUR USER NAME :-  ")
password = input("ENTER YOUR PASSWORD :-  ")


if (user_name, password) not in bet_database:
    bet_database.append((user_name, password))
    print(" Registered successfully! You are now logged in.")
    print(bet_database)
else:
    print(" Login successfully!")

