
import random
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+{}[]|\\:;\"'<>,.?/")
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = list("0123456789")
special_characters = list("!@#$%^&*()-_=+{}[]|\\:;\"'<>,.?/")
all_char = lowercase_letters + uppercase_letters + digits + special_characters
password_ = []
password_len = int(input("ENTER PASSWORD  LEN :-  "))
for passw in range(password_len):
    password = random.choice(all_char)
    password_.append(password)

final = ''.join(password_)
print("YOUR FINAL PASSWORD IS ",final)