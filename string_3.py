mail = input("ENTER A EMAIL:- ")


if "@" in mail  and mail.endswith((".com",".in")):
    print("CORRECT EMAIL")
else:
    print("WRONG EMAIL")
