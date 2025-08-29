print('''_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|  '''   )

cal = True
while cal:
    first_num = int(input("enter your first number :- "))

    operator = input("enter any operator \n 1.+ \n 2.- \n3.* \n4.% \n :->")

    second_num = int(input("Enter your second number :- "))

    if operator == "+":
        print(f"TOTAL=={first_num + second_num}")

    elif operator == "-":
        print(f"TOTAL=={first_num - second_num}")

    elif operator == "*":
        print(f"TOTAL=={first_num * second_num}")

    elif operator == "/":
        print(f"TOTAL=={first_num / second_num}")

    else:
        print("select corecct operator")

    continue_ = input("want you contonue if yes type y if no type n").lower()
    if continue_ == "y":
        cal = True
    else:
        cal =False
    