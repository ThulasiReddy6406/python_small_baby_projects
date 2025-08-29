def life_left(age):
    total_age = 90
    your_age = total_age -age
    your_age_in_weeks = your_age*52
    print(f"you have {your_age_in_weeks} weeks left")

print(life_left(50))