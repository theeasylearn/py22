'''
    write a program to get gap between 2 given dates in days.
    steps
    1) create variable year,month, date
    2) accept 1st date from user
    3) accept 2nd date from user
    4) findout timestamp of both date and store into variables
    5) get difference between two timestamp 
    6) convert gap into days 
    7) display days
'''
from datetime import datetime
import math
#accept day, month and year of birthdate from user, create object of date type & return
def getDate():
    year = int(input("Enter birth year"))
    month = int(input("Enter birth month"))
    day = int(input("Enter birth date(day of month)"))
    temp_date = datetime(year,month,day)
    return temp_date

#accept 1st date from user 
first_date = getDate()

#accept 2nd date from user 
second_date = getDate()

timestamp1 = first_date.timestamp()
timestamp2 = second_date.timestamp()
print(timestamp1,timestamp2)
difference = math.fabs(timestamp1 - timestamp2)
days = ((difference/ 60) / 60) / 24 
print(days)