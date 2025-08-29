# i = 0
# while True :
#     print(i)
#     i = i + 1
#     if ( i % 100 == 0 ):
#         break

# Automatically closes the file
# with open('file.txt', 'w') as f:
#     f.write("Hello, world!")

# print(f)


# f = open('file.txt','w')
# m = f.write("hi my name iis nani this is my new file ")
# f.close()

# f = open('file.txt','r')
# t = f.read()
# print(t)

# f = open('file.txt','a')
# try:
#     f = open("WIN_20250208_04_40_45_Pro.jpg","+rb")
#     r = f.read()
#     print(r[ : 50])
# except FileNotFoundError:
#     print("file not found")
# else:
#     print("wow")
# finally:
#     raise Exception

from PIL import Image
image = Image.open("ch"".jpg")
image.show()