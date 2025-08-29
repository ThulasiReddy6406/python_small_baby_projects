

alphabets =[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
go =True
while go:
    direction = input("choose to encrypt or decrypt").lower()
    text = input("enter your text").upper()
    shift = int(input("choose how many shifts you want "))

    alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# direction = input("Choose to 'encrypt' or 'decrypt': ").lower()
# text = input("Enter your text: ").upper()  # Convert input to uppercase
# shift = int(input("Choose how many shifts you want: "))

    def caesar_cipher(original_text, shift_amount, mode="encrypt"):
        ceaser = ""

        for letter in original_text:
            if letter in alphabets:
                old_index = alphabets.index(letter)
            
                if mode == "encrypt":
                    new_index = (old_index + shift_amount) % 26  # Ensures wrap-around
                elif mode == "decrypt":
                    new_index = (old_index - shift_amount) % 26  # Reverse shift
            
                ceaser += alphabets[new_index]
            else:
                ceaser += letter  # Preserve spaces or special characters
    
        print(f"Result: {ceaser}")
    

    # Call function based on user choice
    if direction == "encrypt":
         caesar_cipher(text, shift, mode="encrypt")
    elif direction == "decrypt":
         caesar_cipher(text, shift, mode="decrypt")
    else:
          print("Invalid option. Please enter 'encrypt' or 'decrypt'.")
    restart = input("yes if you want to end  or no")
    if restart == "yes":
        go =False
    