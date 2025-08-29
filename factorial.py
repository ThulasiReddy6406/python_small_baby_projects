def factorial(num):
    if num < 0 :
        return "invalid";
    result =1
    for i in range(1,num+1):
        result*=i
    return result;
    
    
num = int(input("enter  a number"))
print(f"your result is{factorial(num)}")

        
        