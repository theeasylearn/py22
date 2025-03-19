# rename a file
import os

# os.rename('./myfolder/LESSON1.txt','./myfolder/lesson1.py')

print("rename successfuly....")

# cut file - myfolder - temp
# os.rename('./myfolder/lesson1.py','./lesson2.txt')

os.remove('lesson2.txt')
print("file deleted successfuly")