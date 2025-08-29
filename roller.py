print("welcome to roller coster")
totalcost =0
age=int(input("age :"))
print(age)
if(age<18):
    print("not allow")
elif(age>18):
    print("allow")
if(age>=18 and age<=25):
    print("ticket price = 10")
    totalcost+=10
elif(age>25 and age<=50):
    print("ticket price = 20")
    totalcost+=20
else:
    print("ticket price = free")
photo=input("photo = yes or no")
if (photo=="yes"):
    print("cost = 5")
    totalcost+=5
    print("totalcost:",totalcost,"$")
else:
    print("cost = 0")
    print(totalcost)
    




    
