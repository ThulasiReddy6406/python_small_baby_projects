print(" WELCOME TO TREASURE ISLAND \n YOUR MISSION IS TO FIND THE TREASURE")
direction = input("choose your direction left or right :-  ")
if direction == "left":
    print("you won 1st step")
    choose = input("choose to swim or wait to win second step :- ")
    if choose == "wait":
        print("you won 2nd step")
        final =input("choose a room 1.red , 2.blue , 3.yellow :- ")
        if final == "yellow":
            print("you won the hunt buddy!")
        elif final == "red":
            print("burned by fire")
        elif final == "blue":
            print("eaten by beast game over !")
        else:
            print("GAME OVER!")
    else:
        print("attacked by trout game over!")
else:
    print("FALL INTO HOLE GAME OVER!")