try :     
    a = int(input("enter number 1 : "))
    b = int(input("enter number 2 : "))
    
except(KeyError , ValueError , IndexError) :
    print("error....")
    
else:
    print("addition : ",a+b)
    
finally:
    print("this code must run....")
    