def cheak():
     word = "+++"
     with open ("file.txt","r") as f:
          data = f.read()
          if (data.find(word) != -1):
               print("!!!!!!!!!!")
          else:
               print("@@@@@@@@")


def cheak_line():
     word = "python"
     line = 1
     data = True
     with open("file.txt","r") as f:
          while data:
               data=f.readline()
               if(word in data ):
                    print(line)
                    return
               line+=1          
                  
cheak_line()
