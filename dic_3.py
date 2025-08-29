# calander = {}
# many = int(input("HOW MANY EVENTS DO YOU WANT TO ADD :-  "))
# def add():
#     date = int(input("ENTER THE DATA :-  "))
#     event = list(input("ENTER EVENTS:-  ").split())
#     calander[date] = {  "event" : event  }
# for i in range(many):
#     add()

# def update():
#     date = int(input("ENTER THE DATE:- "))
#     event = list(input("ENTER updated EVENTS:-  ").split())
#     if date in calander:
#         calander[date] = {
#             "event" : event
#         }
# update()

# print(f"new list :- {calander}")
# print(calander[23])
# del calander[23]

# sen = input("ENTER THE SENTENSE :-  ")
# words = sen.split()
# freq = {}

# for word in words:
#     freq[word] = freq.get(word,0)+1
# print(freq)




conatact = {}
how = int(input("HOW MANY DO YOU WANT TO ADD:- "))
def add():
    name = input("ENTER YOUR NAME:-  ")
    number = input("ENTER YOUR NUMBER :-")
    conatact[name] = number
for i in range(how):
    add()
# print(conatact)

def search():
    name = input("name :- ")
    if name in conatact:
        print(conatact[name])
search()





















