amount = 0
def addMoney(rupees):
    global amount #it will ask interpreter to use global variable amount
    # amount = 0 #create new amount variable which is local so it will not effect global variable
    amount = amount + rupees

rupees = int(input("Enter rupees"))
print(f"Amount before calling function {amount}")
addMoney(rupees)
print(f"Amount after calling function {amount}")
