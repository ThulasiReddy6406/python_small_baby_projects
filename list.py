# n = 3
# movies = tuple(map(str, input(f"Enter {n} movie names: ").split()))

# if len(movies) != n:
#     print(f"Please enter exactly {n} movies.")
# else:
#     print(movies)

list = [1,3,3,1]

list_1 = list.copy()
list_1.reverse()

if (list_1== list):
    print("palindrome")
else:
    print("not palindrome")