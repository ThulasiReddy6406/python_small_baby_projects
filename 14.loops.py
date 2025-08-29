# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*" , end = " ")
#     print()
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''
  
  
  
#for i in range(1,6):                                      
#  for j in range(1,6-i):
#        print("*", end = " ")
 #   print()
'''

* * * * 
* * * 
* * 
*

'''

#reversing the array

#arr = [1, 2, 3, 4, 5]
#reversed_arr = []
#for i in range( 4,-1,-1):
#    reversed_arr.append(arr[i])
#print(reversed_arr)

'''   [5, 4, 3, 2, 1]  '''


''' Create a program that uses a loop to simulate
rolling two dice until the sum of their numbers equals 10.'''

'''import random

go = True
while go:
    two_dice = (random.randint(1, 6), random.randint(1, 6))  # Rolling the dice
    total = sum(two_dice)  # Calculating the sum of the dice
    print(f"Rolled: {two_dice}, Total: {total}")  # Printing the dice and total
    if total == 10:  # Check if the sum equals 10
        go = False
        print("The dice sum equals 10!")'''

'''
# FINDING 2ND LARGEST NUM 
num =[1,2,3,4,5,6,7,8,9,10]

lar_num = 0

for i in num:
    if i > lar_num:
        lar_num = i
        

sec_lar = 0
for j in num:
     if  j>sec_lar and j < lar_num:
         sec_lar = j
print(f"SECOND LARGEST NUMBER :- {sec_lar}")
'''

'''
for i in range(0,5):
    for j in range(0,5):
        print("*",end="" )
    print()
    
*****
*****
*****
*****
*****
'''

'''
for i in range(0,5):
    for j in range():
        print("*", end = " ")
    print()
    
'''


'''
rows = 5  # Number of rows for the triangle
for i in range(1, rows + 1):  # Outer loop for rows
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # Move to the next line after each row

    *
   ***
  *****
 *******
*********
'''



    
