class calculation:
    def multiplication(self):
        return 0
        
    def multiplication(self,a):
        return a*a
        
    def multiplication(self,a,b):
        return a*b
    
obj = calculation()

n = int(input("1->single value\n2 -> multi value :"))
if n==1:
    a = int(input("enter a number : "))
    print(obj.multiplication(a,a))

elif n==2:
    a = int(input("enter a number1 : "))
    b = int(input("enter a number2 : "))
    print(obj.multiplication(a,b))
    
else:
    print(obj.multiplication(0,0))