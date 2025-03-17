# voting system

try:
    age = int(input("enter your age : "))

    if age>18:
        print("you can vote")
        
    else:
        raise ValueError

except ValueError:
    print("you are below 18...")

print("good bye...")

