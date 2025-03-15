import os
while True:
    file_name = input("Enter file name")
    mode = 'r' #read mode 
    #open file
    try:
        file_content = open(file_name,mode)
        #read content line by line
        count=0
        for line in file_content:
            print(line,end='')
            count+=1
        print()
        print(f"{file_name} has {count}")
        break
    except FileNotFoundError:
        print("no such file exists..")
    except PermissionError as error:
        if os.path.isdir(file_name):
            print("this is folder not a file")
        else:
            print("you dont have permission to read this file")
print("Good bye...")