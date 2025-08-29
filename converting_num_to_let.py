print("WELCOME TO NUM CONVERTER!!!")
num = input("ENTER A NUMBER:-  ")
digits_to_words = {
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine"
}
print("ends here :- ",end="")
for digits in num:
    if digits in digits_to_words:
        print(digits_to_words[digits],end = " ")
    else:
        print("INVALID NUM !!!")