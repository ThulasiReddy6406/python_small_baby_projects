
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

com = True
while com:

    choice = input("ENTER ENCODE OR DECODE :-  ").lower()
    msg = input("ENTER YOUR MESSAGE :-  ").lower()
    shift = int(input("enter your shift :-  "))


    def encode(original_text,shift_number):
        ceaser_cipher =''
        for letter in original_text:
            position=(alphabets.index(letter) + shift_number)
            position %= len(alphabets)
            ceaser_cipher += alphabets[position]
        return ceaser_cipher


    def decode(shifted_position_text,shift_number_):
        ceaser_cipher = ''
        for let in shifted_position_text:
            shifted_one=alphabets.index(let) - shift_number_
            shifted_one %= len(alphabets)
            ceaser_cipher += alphabets[shifted_one]
        return ceaser_cipher


    if choice == "encode":
        result = encode(msg, shift)
        print(f"Encoded Message: {result}")

    elif choice == "decode":
        result = decode(msg, shift)
        print(f"decoded message :{result}")

    else:
        print("enter correct one")


    complete = input("DO YOU WANT TO COMPLETE 1.yes or 2.no").lower()

    if complete == "no":
        com = False

    else:
        com = True

