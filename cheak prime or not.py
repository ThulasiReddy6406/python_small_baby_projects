def check_prime(num):
    if num <= 1:
        return "not prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "not prime"
    return "prime"

num = int(input("Enter a number: "))
print(f"The number {num} is {check_prime(num)}")
