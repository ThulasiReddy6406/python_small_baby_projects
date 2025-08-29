height = int(input("enter your height in cm :- "))
bill = 0 

if height >120:
    print("can ride")
    age = int(input("enter your age :- "))
    if age <12:
        bill +=5
        print("you cost 5 rupees")
    elif age > 12 and age <18:
        bill += 7
        print("you cost 7 rupees")
    else:
        bill += 12
        print("you cost 12 rupees")

    photo = input("you want photo yes or no!")

    if photo == "yes":
         bill +=3
         print("3 rupees for photo")
         print(f"TOTAL BILL :- {bill}")
    else:
        print(f"TOTAL BILL :- {bill}")


else:
    print("cant ride")

