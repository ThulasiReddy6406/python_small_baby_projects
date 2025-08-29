# ANAGRAM CHEAKER 
string_1 = input("ENTER A STRING :- ")
string_2 = input("ENTER ANOTHER STRING :- ")
#used .replace(" ","") to clear all the spaces and .lower() for lower alphabets
string_1 = string_1.replace(" ","").lower()
string_2 = string_2.replace(" ","").lower()
#sorted() used for sorting
sort_1 = sorted(string_1)
sort_2 = sorted(string_2)

if sort_1 == sort_2 :
    print("anagram")
else:
    print("not anagram")   

''' use example  string_1 = silent and string_2 = listen 
anagram cheaker will cheak both words has same letters or not .'''