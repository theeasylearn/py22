'''
    write a program to findout whether given year is leap year or not.
    take year as input
    decide whether particular year is leap year or not.
     If a year is evenly divisible by 4, but it is not evenly divisible 100, then it is a leap year.
     if year is divisible by 100 and 400 then it leap year otherwise it is not leap year
'''
year = int(input("Enter year"))
reminder1 = year % 4
reminder2 = year % 100
reminder3 = year % 400
if reminder1==0 and reminder2!=0:
    print(f"{year} is leap year")
else:
    if reminder2==0 and reminder3==0:
        print(f"{year} is leap year")
    else: 
        print(f"{year} is not leap year")
