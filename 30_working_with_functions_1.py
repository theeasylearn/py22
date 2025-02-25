#concept of user defined functions()
#with argument with return value 
def getSquare(number):
    #square is local variable (can be accessed only inside function)
    square = number * number
    return square

#without argument with return value
def getPi():
    pi = 3.1415 #local variable 
    return pi 

#without argument without return value 
def printDate():
    print("Tuesday 25-02-2025")

#with argument without return value
def printDay(dayOfWeek):
    if dayOfWeek == 1:
        print("Monday")
    elif dayOfWeek == 2:
        print("Tuesday")
    elif dayOfWeek == 3:
        print("Wednesday")
    elif dayOfWeek == 4:
        print("Thursday")
    elif dayOfWeek == 5:
        print("Friday")
    elif dayOfWeek == 6:
        print("Saturday")
    elif dayOfWeek == 7:
        print("Sunday")

#call function(run function)
number = int(input("Enter number"))
square = getSquare(number)
print(f"square of 10 = {square}")

pi = getPi()
day = int(input("Enter day of week"))
printDate()
printDay(day)
