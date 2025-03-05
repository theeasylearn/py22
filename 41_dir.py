import datetime
import math 
import sys 
def showMethods(module):
    list = dir(module)
    print("----------------------------------------------------------------")
    print(f"method in math {module}")
    for item in list:
        print(item)

showMethods(datetime)
showMethods(math)
showMethods(sys)
