students ={
  1 : {
    "name": "John",
    "age": 19,
    "subject": {"Math": 85, "Science": 90, "English": 78},
      }
}
want_to_add = input("WANT YOU ADD STUDENTS :-  ")
if want_to_add == "yes":
    add = True
    while add:
        roll_no = int(input("ENTER YOUR ROLL_NO :-  "))
        name = input("ENTER YOUR NAME :-  ")
        subjects = ["Math", "Science", "English"]
        marks_in = list(map(int,input("ENTER YOUR MARKS BY SEPERATE").split()))
        marks = dict(zip(subjects,marks_in))
        students[roll_no] = {
        "name": name,
        "roll" : roll_no,
        "marks": marks
         }
        con = input("WANT YOU TO ADD ANOTHER STUDENT DETAILS :-  ")

        if con == "yes":
            add = True
        else:
            add = False
            break
else:
    print(None) 

print(students)