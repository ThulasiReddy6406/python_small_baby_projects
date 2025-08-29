students = {}
avg = 0 
def add_name_marks(name,marks):
    students[name] = {
        "Telugu" : marks[0],
        "hindi" : marks[1],
        "English" : marks[2]
    }
for i in range(5):    
    name = input("ENTER YOUR NAME:-  ")
    marks = list(map(int,input("ENTER YOUR MARKS :-  ").split()))
    add_name_marks(name,marks)

for n,m in students.items():
    print(f"{n}-->{m}")

def average(name):
    if name == students[name]:
        total = marks["Telugu"] + marks["hindi"] + marks["English"]
        avg = total / 3
        print(f"Average marks of {name} is {avg}")
    
n = input("ENTER YOUR NAME:- ")
average(n)