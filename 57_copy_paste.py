# 2 inputs - copy file - paste file name

copy = input("enter file name to copy : ")
paste = input("enter file name to paste : ")

# copy file data
file1 = open(copy,"r")
data = file1.read()

file1.close()
print("copy successfuly....")

# paste file data
file2 = open(paste,"w")
file2.write(data)

file2.close()

print("paste successfuly....")
