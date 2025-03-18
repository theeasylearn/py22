name = input("enter file name : ")
content = input("enter file content to write : ")


obj = open(name,"w")

obj.write(content)

obj.close()

print("data writen in file....")

