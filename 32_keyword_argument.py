#example of keyword arguments
def getPi():
    return 3.1415

def getSquare(number):
    return number * number
def getCylinderVolume(radius,height):
    #local variable
    volume = getPi() * getSquare(radius) * height
    return volume

r = int(input("Enter cylinder radius"))
h = int(input("Enter Cylinder height"))
#using keyword arguments
volume = getCylinderVolume(height=h,radius=r)
print(volume)

