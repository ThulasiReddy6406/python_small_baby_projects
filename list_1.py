c_book =[]

name = input("ENTER YOUR NAME:-  ")
num = int(input("ENTER YOUR NUMBER:-  "))
yes = False
while True:
    for contacts in c_book:
        if contacts[0]==name or contacts[1]==num:
            yes=True
            print("ALREADY REGISTERED")
            print(f"{contacts[0]}---->{contacts[1]}")
            break

    if not yes :
        c_book.append((name,num))
        print("contact saved")


    con = input("DO YOU WANT TO ADD ANOTHER CONTACT:-  ")
    if con == "yes":
        True
    else:
        print(c_book)
        break
