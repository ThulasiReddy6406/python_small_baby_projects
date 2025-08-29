'''print("||| Student Management System |||")

students = {
    1 : {
        "name" : "THULASI REDDY",
        "marks" : [10,20,30]
        },
    2 : {
        "name" : "jashwanth",
        "marks" : [20,30,40]
        },
    3 : {
        "name" : "reddy",
        "marks" : [40,50,60]
        }
}

for n,m in students.items():
    print(f"{m}") 
new_dic = {}
def add_students():
    roll_no = int(input("ENTER YOUR ROLL NO :- "))
    name = input("ENTER YOUR NAME :- ")
    marks = list(map(int, input("ENTER YOUR MARKS (space separated) :- ").split()))
    new_dic[roll_no] = {
        "name" : name,
        "marks" : marks
    }
for i in range(3):
    add_students()

students.update(new_dic)

print(students)

def search(roll_no):
    for k,v in students.items():
        k == roll_no
        print(students[roll_no])
        break
roll = int(input("ROLL NO:- "))
search(roll)

def update(roll_no,marks):
     for k,v in students.items():
        k == roll_no
        students[roll_no] = {
            "name" : students[roll_no]["name"],
            "marks" : marks
        }
roll_no = int(input("ENTER YOUR ROLL_NO :- "))
marks = list(map(int, input("ENTER YOUR MARKS (space separated) :- ").split()))
update(roll_no,marks)


def delete(roll):
        if roll in students:
              del students[roll]

roll = int(input("ENTER ROLL NO :- "))
delete(roll)
print(students)'''

''' IF YOU WANT CHOICES WHICH OPERATION DO YOU WANT TO PERFORM 
USE LOOP FOR IT ....


'''