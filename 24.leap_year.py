def leap_year(year):
    if year % 4 == 0:
        print("it is a leap year")
    elif year % 100 !=0:
        print("it is a leap year")
    elif year % 400 == 0:
        print("it is a lea year")
    else:
        print("it is not a leap year")
leap_year(2024)