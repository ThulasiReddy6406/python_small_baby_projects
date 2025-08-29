students = [23,34,25,65,36,643,63,63,62,864,4256,]


high = max(students)
print(high)

total = sum(students)
print(total)

min_score = min(students)
print(min_score)

total_score =0
for score in students:
    total_score+=score
print(f"total_score{total_score}")

max_score =0


for score in students:
    if score >= max_score:
        max_score = score
print(f"max_score{max_score}")
    
    
min_score = 100000

for score in students:
    if score <= min_score:
        min_score = score
print(f"min_score is {min_score}")
    