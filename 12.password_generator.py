print("WELCOME TO PASSWORD GENERATOR")

import string
import random

# Alphabets
uppercase_alphabets = string.ascii_uppercase  
lowercase_alphabets = string.ascii_lowercase  
all_alphabets = string.ascii_letters          
# Numbers
numbers = string.digits                      

# Special Characters
special_characters = string.punctuation      

alpha = int(input("HOW MANY ALPHABETS YOU WANT"))
numb = int(input("how many numbers you want"))
special = int(input("how many special characters you want"))

#------------------- easy method -------------------#
# password = ""
# for char in range(1,alpha+1):
#     password += random.choice(all_alphabets)

# for num in range(0,numb+1):
#     password += random.choice(numbers)

# for spe in range(0,special+1):
#     password += random.choice(special_characters)

# insert = password
# print(insert)

#----------------------hard method --------------------#

password = []

for char in range(0,alpha+1):
    password.append(random.choice(all_alphabets))

for num in  range(0,numb+1):
    password.append(random.choice(numbers))

for spe in range(0,special+1):
    password.append(random.choice(special_characters))

bef_shuff = password
print(bef_shuff)

random.shuffle(bef_shuff)
print(bef_shuff)

new_pass = ""
for i in bef_shuff:
    new_pass+=i

print(new_pass)

#------------------------------------ completed pass word generator --------------------------------------#
 