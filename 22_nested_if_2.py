'''
    write a program to findout how many days given month has 

    step 
     take month from user as input 
     first month is valid between 1 t0 12, if not display message
        if month is 1, 3, 5, 7, 8, 10, 12 it has 31 days 
        if month is 4 6 9 11 it has 30 days 
        else month has 28 to 29 days

'''
month = int(input("Enter month"))
if month<0 or month>12:
    print("it is not valid month")
else:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print(f"{month} has 31 days")
    elif month==4 or month==6 or month==9 or month==11:
        print(f"{month} has 30 days")
    else:
        print(f"{month} had 28/29 days")

print("Good bye...")