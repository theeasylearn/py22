name = input("enter file name : ")
data = input("enter file data : ")

file = open(name,"a")

choise = int(input("1 for new line & 2 for same line :  "))
if choise==1:
    file.write("\n"+data)

elif choise==2:
    file.write(" "+data)

file.close()

print("data writen....")
