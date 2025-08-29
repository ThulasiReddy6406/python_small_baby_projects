student_name = input("STUDENT NAME:- ")
marks =[]
subjects =["tel","hin","eng","mat","sci"]
for i in range(5):
    mark = int(input(f"STUDENT MARKS in {subjects[i]} :- " ))
    marks.append(mark)
avg = sum(marks)/5
if (avg>=90):
    grade = "A"
elif (avg >=70 and avg<90):
    grade ="B"
elif (avg <= 7):
    grade = "C"
else:
    grade = "F"
students = (student_name,[marks],avg,grade)
print(f"STUDENT NAME:-{student_name}""\n"
      f"STUDENT MARKS:-{marks}""\n"
      f"STUDENT  AVERAGE :-{avg}""\n"
      f"STUDENT GRADE :-{grade}")
