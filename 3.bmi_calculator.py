weight = int(input("Enter your weight :-"))
height = float(input("Enter your height :-"))
bmi = weight / (height ** 2)

print(round(bmi))

if bmi <18.5:
    print("under weight")
elif bmi>18.5 and bmi<25:
    print("normal weight")
elif bmi == 25:
    print("over weight")
else:
    print("invalid error")