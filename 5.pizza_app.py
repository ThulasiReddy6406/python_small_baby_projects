from re import I


print("welcome to pizza delivery")

size = input("What size of pizza you want L OR M OR S")

cost = 0

if size == "s":
    print("it costs 10 rupees")
    cost += 10

elif size == "m":
    print("it costs 20 rupees")
    cost += 20

elif size == "l":
    print("it cost 30 rupees")
    cost += 30

else:
    print("choose coreect one ")



peppor = input("do you want perror do you want  y or n")

if peppor == "y":
    print("it costs 10 rupees extra")
    cost +=10
    print(f"bill with perror {cost}")
else:
    print(f"bill with perror {cost}")

extra_cheese = input("do you want cheese  ? y or n")

if extra_cheese == "y":
    print("it costs 10 rupees extra")
    cost +=10
    print(f"your total bill is =={cost}")

else:
    print(f"your total bill is =={cost}")



