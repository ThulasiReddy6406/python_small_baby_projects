('''                                                                           
                                                                           
    ,---,                   ,----..    ,----..     ,---,       ,-.----.    
  .'  .' `\           ,--, /   /   \  /   /   \   '  .' \      \    /  \   
,---.'     \        ,'_ /||   :     :|   :     : /  ;    '.    ;   :    \  
|   |  .`\  |  .--. |  | :.   |  ;. /.   |  ;. /:  :       \   |   | .\ :  
:   : |  '  |,'_ /| :  . |.   ; /--` .   ; /--` :  |   /\   \  .   : |: |  
|   ' '  ;  :|  ' | |  . .;   | ;    ;   | ;    |  :  ' ;.   : |   |  \ :  
'   | ;  .  ||  | ' |  | ||   : |    |   : |    |  |  ;/  \   \|   : .  /  
|   | :  |  ':  | | :  ' ;.   | '___ .   | '___ '  :  | \  \ ,';   | |  \  
'   : | /  ; |  ; ' |  | ''   ; : .'|'   ; : .'||  |  '  '--'  |   | ;\  \ 
|   | '` ,/  :  | : ;  ; |'   | '/  :'   | '/  :|  :  :        :   ' | \.' 
;   :  .'    '  :  `--'   \   :    / |   :    / |  | ,'        :   : :-'   
|   ,.'      :  ,      .-./\   \ .'   \   \ .'  `--''          |   |.'     
'---'         `--`----'     `---`      `---`                   `---'       
                                                                           ''')
import random

print("WELCOME TO NUMBER GUESSING GAME BUDDYS")

my_num = random.randint(1, 101)
print(my_num)

choose = input("CHOOSE A DIFFICULTY . TYPE 'EASY' OR 'HARD': ").lower()

if choose == "easy":
    choices = 10
elif choose == "hard":
    choices = 5
else:
    print("Invalid choice. Defaulting to 'hard'.")
    choices = 5

com = True

def find_num(num):
    global choices
    if num == my_num:
        print("YOU ROCKED IT BUDDY! You guessed it.")
        return True
    elif num > my_num:
        print("Too high!")
        print("Guess again.")
        choices -= 1
    elif num < my_num:
        print("Too low!")
        print("Guess again.")
        choices -= 1
    return False

while com:
    print(f"Remaining choices: {choices}")
    number = int(input("ENTER YOUR NUMBER: "))
    if find_num(number) == True:
        com = False
    
    if choices == 0:
        com = False
        print(f"You're out of guesses! The number was: {my_num}")

print("Game Over")
