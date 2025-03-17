try :     
    a = int(input("enter number 1 : "))
    b = int(input("enter number 2 : "))
    print("addition : ",a+b)

    l1 = [1,2,3,4]
    for i in range(0,6):
        print(l1[i])

except ValueError:
    print("enter a valid number....")
    
except IndexError:
    print("index is not valid....")
    
except:
    print("error")