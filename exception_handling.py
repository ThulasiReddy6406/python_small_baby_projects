# def add(a,b):
#     try:
#         return a+b
        
#     except ZeroDivisionError:
#         print("zero cant be divided")
#     except Exception:
#         return "input must be num"
#     except ValueError:
#         print("enter the number")
#     except ArithmeticError:
#         print("enter num")
#     else:
#         print("SUCCESS")
#     finally:
#         print("RUN ALWAYS")
# print(add(3,5))
# print(add(3,'a'))

# def divide_numbers(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero."
#     except TypeError:
#         return "Inputs must be numbers."
#     else:
#         print("Division successful.")
#     finally:
#         print("Execution complete.")

# print(divide_numbers(10, 0))
# print(divide_numbers(10, 'a'))


# try:
#     # some risky code
#     x = int("man")  # ValueError
# except Exception as e:
#     print("An error occurred:", e)
# else:
#     print(x)