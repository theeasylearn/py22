'''
    write a program to findout whether given number is prime or not 
    accept number from user 
    1 create variable divisor store 2 in it 
    2 divide number by divisor and store reminder into reminder variable
    3 if reminder is zero stop the process and display message number is not prime number 
    4 otherwise increase divisor by 1  repeat 2 to 4 step till divisor is less then number 

'''
number = int(input("Enter number to check is it prime number?")) # 7
count=0
if number!=2 and number%2==0:
    print(f"{number} is not prime number")
else:
    divisor = 2 
    half = number // 2
    while divisor<half:
        count+=1
        reminder = number%divisor # 6%2=0 
        if reminder==0:
            print(f"{number} is not prime number")
            break
        divisor=divisor+1
    if  divisor==half or number==2:
        print(f"{number} is prime number")
print(count)