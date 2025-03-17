file = open("demo.txt","r")
# print(file)

# for i in file:
#     print(i)

# read whole file
print(file.read())

# read specific character in file
print(file.read(5))
    
file.close()