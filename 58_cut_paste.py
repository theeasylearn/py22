# 2 inputs - copy file - paste file name

cut = input("enter file name to cut : ")
paste = input("enter file name to paste : ")

# copy file data
file1 = open(cut,"r")
data = file1.read()
file1.close()

file1 = open(cut,"w")
file1.write("")
file1.close()
print("cut successfuly....")


# paste file data
file2 = open(paste,"a")
file2.write("\n"+data)

file2.close()

print("paste successfuly....")
