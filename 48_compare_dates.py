'''
    write a program to accept date of birth of two brother. and find elder brother
    steps
    1) create variable year,month, date
    2) accept 1st brother birthdate in variable year, month, date 
    3) create object1 using datetime.date() class use variable year, month & date
    4) accept 2nd brother birthdate in variable year, month, date 
    5) create object2 using datetime.date() class use variable year, month & date
    6) compare object1 and object2 to findout elder brother
'''
from datetime import date
#accept day, month and year of birthdate from user, create object of date type & return
def getDate():
    year = int(input("Enter birth year"))
    month = int(input("Enter birth month"))
    day = int(input("Enter birth date(day of month)"))
    temp_date = date(year,month,day)
    return temp_date

#accept 1st brother date of birth 
brother1 = getDate()

#accept 2nd brother date of birth 
brother2 = getDate()

print(brother1)
print(brother2)

#compare 
if brother1<brother2:
    print("Brother 1 is elder brother")
else:
    print("Brother 2 is elder brother")

