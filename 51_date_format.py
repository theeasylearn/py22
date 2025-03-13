from datetime import datetime, timedelta

now = datetime.now();
birthdate = input("Enter your birthdate(YYYY-mm-dd)")
# print(birthdate)
actualDate = datetime.fromisoformat(birthdate)
print(actualDate)
print("Indian format date")
print(actualDate.strftime("%d-%m-%Y"))
print("US format date")
print(actualDate.strftime("%m-%d-%Y"))

#adding days into date 
newDate = actualDate + timedelta(days=365)
print(newDate)

#subtract days into date 
oldDate = actualDate - timedelta(days=365)
print(oldDate)