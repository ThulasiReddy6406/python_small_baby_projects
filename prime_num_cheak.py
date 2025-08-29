num = int(input("ENTER A NUMBER :-  "))

for i in range(1,num):
    if i % 1 ==0 and i % i == 0 and i % i+1 != 0:
        print("PRIME")
    else:
        print("nnot") 