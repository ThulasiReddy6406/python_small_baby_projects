number1=int(input("enter a random number"))
number2=int(input("enter another random number"))
operator=input("enter the operator")
# if(operator=="+"):
#     print("sum=",number1+number2)
# elif(operator=="-"):
#     print("diff=",number1-number2)
# elif(operator=="*"):
#     print("multi=",number1*number2)
# elif(operator=="/"):
#     print("div=",number1/number2)
# else:
#     print("error")

print(
    f" sum= {number1 + number2}" if operator == "+" else "no",
    f" diff={number1 - number2}" if operator == "-" else "no",
    f" multi={number1 * number2}" if operator == "*" else "no",
    f" divi={number1 / number2}" if operator == "/" else "no"
)
