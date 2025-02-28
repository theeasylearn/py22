#function that return multiple value
def doProcess(num1,num2):
    #local variable
    addition = num1 + num2 
    subtraction = num1 - num2 
    multiplication = num1 * num2 
    division = num1 / num2 
    #return multiple variable using comma as separator 
    return addition, subtraction, multiplication, division

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

#result is tuple which has multiple value return by function
result = doProcess(num1,num2)
print(result)

