def add(n1,n2):
    return n1+n2

def subract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operations = {
    
    "+" : add,
    "-" : subract,
    "*" : multiply,
    "/" : div,
}

f_num = int(input("enter your first number"))
go = True

while go :
    
    operation = input("SELECT YOUR OPERATION")
    s_num = int(input("select your second number"))
    result = operations[operation](f_num,s_num)
    print(f"{f_num} {operation} {s_num} = {result}")
    
    try_again = input(f" if you want to continue with last result give yes/or/no?{result}").lower()
    
    if try_again == "no":
        go = False
    elif try_again == "yes":
        f_num = result
        
    else:
        go = false
    
    
'''    def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division,
}

con = True
f_num = int(input("Enter your first number: "))  # Move initial input outside the loop

while con:
    for symbol in operations:
        print(symbol)
    choose_operation = input("Choose the operation: ")
    s_num = int(input("Enter your second number: "))
    result = operations[choose_operation](f_num, s_num)
    print(f"{f_num} {choose_operation} {s_num} = {result}")
    
    want_to_con = input(f"Do you want to continue with the result {result}? (yes/no): ").lower()
    if want_to_con == "no":
        con = False
    elif want_to_con == "yes":
        f_num = result
    else:
        con = False
        '''