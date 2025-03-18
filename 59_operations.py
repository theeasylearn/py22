# find no characters in file
name = input("enter name of file : ")

file = open(name,"r")

data = file.read()
# print(type(data))
# a = "hello"
print(len(data))

count = 0
for i in data:
    # print(i)  
    count+=1
    
print(count)

file.close()