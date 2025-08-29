import os

with open("file.txt",'r+') as f:
    data = f.read()
new = data.replace("java","python")
print(new)

with open("file.txt","w") as d:
     d.write(new)

