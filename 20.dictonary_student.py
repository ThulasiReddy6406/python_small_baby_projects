student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student , scores in student_scores.items():
    if scores < 100 and scores > 91:
        student_grades[student]="Outstanding"
        
    elif scores < 90 and scores > 81:
        student_grades[student]="Exceeds Expectations"
        
    elif scores < 80 and scores > 71:
         student_grades[student]="Acceptable"
         
    else:
         student_grades[student]="Fail"
         
         
print(student_grades)
        



