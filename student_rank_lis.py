# created a list named student
students = []

#add students to the list 

def add_students():
    name = input("ENTER YOUR NAME:- ")
    roll_no = int(input("ENTER YOUR ROLL_NO:- "))
    marks = int(input("ENTER YOUR TOTAL MARKS:-  "))
    new_student = ((name,roll_no,marks))
    students.append(new_student)


def view_students():
    for student in students:
        print(students)
    else:
        print("student not found")


def update_student():
    name = input("ENTER YOUR NAME :- ")
    new_marks = int(input("ENTER YOU NEW MARKS :-  "))
    for i,(n,r,m) in enumerate(students):
        if n == name:
            students[i] =((n,r,new_marks))
            break
    else:
            print("STUDENT NOT FOUND!!!")
        
def delete():
    name = input("ENTER YOUR NAME :- ")
    for i,student in enumerate(students):
        if name == student[0]:
            deleted = students.pop(i)
            print(f"{deleted}is deleted")
            break
    else:
        print("student not found")


def topper():
     top = 0 
     name = ''
     for i , student in enumerate(students):
        if student[2] > top:
            top = student[2]
            name = student[0]
            print("top = {name} with {top}")
        else:
            print("student not found")



def search_by_name():
    name = input("ENTER NAME :-  ")
    for student in students:
        if name == student[0]:
            print(f"{student}")
    else:
        print("student not found")

while True:
    choice = int(input('''CHOOSE WHAT TO DO :-  
    1.Add a student

    2.View all students

    3.Update marks of a student

    4.Delete a student

    5.Display top scorer

    6. search by name    '''))

    if choice == 1:
        add_students()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete()
    elif choice ==5:
        topper()
    elif choice == 6:
        search_by_name()
    else:
        print("choose a right choice 1 to 6")
    ope = input("ANY OTHER OPERATIONS :-  ")
    if ope == "yes":
        True
    else:
        False




print("TRY THIS ")




