#example and concept of logical operators (and, or, not)
num1 = int(input("enter value for num1"))
num2 = int(input("enter value for num2"))
num3 = int(input("enter value for num3"))

result = num1 == num2 and num2 == num3
print("result = num1 == num2 and num2 == num3 ",result)
result = num1 == num2 or num2 == num3
print("result = num1 == num2 or num2 == num3 ",result)
result = not num1 == num2 
print("result = not num1 == num2 ",result)
