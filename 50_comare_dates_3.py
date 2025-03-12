from datetime import datetime

# Accept day, month, and year from user and return a datetime object
def getDate():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter date (day of month): "))
    return datetime(year, month, day)

# Step 1: Accept first date
print("Enter first date:")
first_date = getDate()

# Step 2: Accept second date
print("Enter second date:")
second_date = getDate()

'''
Instead of working with timestamps, you should directly subtract two datetime objects, because Python's datetime module supports direct subtraction and gives you a timedelta object, which makes calculating the difference in days easy and accurate, regardless of whether dates are before or after 1970.
'''
# Step 3: Calculate difference between two dates
difference_in_days = abs((second_date - first_date).days)
difference_in_years = int(difference_in_days / 365 )

# Step 4: Display difference in days
print(f"\nGap between two dates is: {difference_in_days} days")
print(f"\nGap between two dates is: {difference_in_years} year")
