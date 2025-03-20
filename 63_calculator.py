class calculator:
    def addition(self,a,b):
        print(f"addition : {a+b}")
        
    def subtraction(self,a,b):
        print(f"subtraction : {a-b}")
        
    def multiplication(self,a,b):
        print(f"multiplication : {a*b}")
        
    def division(self,a,b):
        print(f"division : {a/b}")
        
    def error(self):
        raise ValueError
        
obj = calculator()

print("1 -> addition\n2 -> subtraction\n3 -> multiplication\n4 -> division")
choise = int(input("enter your choise : "))

if choise==1 or choise==2 or choise==3 or choise==4:
    n1 = int(input("enter number1 : "))
    n2 = int(input("enter number2 : "))

if choise == 1:
    obj.addition(n1,n2)
    
elif choise==2:
    obj.subtraction(n1,n2)
    
elif choise==3:
    obj.multiplication(n1,n2)
    
elif choise==4:
    obj.division(n1,n2)
    
else:
    try:
        obj.error()
        
    except:
        print("please give valid choice!!!")