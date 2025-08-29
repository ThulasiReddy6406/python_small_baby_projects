def reverse_num(number):
    reversed_num = ""
    for i in str(number):
        reversed_num = i + reversed_num 
    print(reversed_num)
        
        
number = 534455
reverse_num(number)