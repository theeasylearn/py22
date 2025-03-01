#example of lambda 
getSquare = lambda num: num * num
getCircleArea = lambda radius : 3.14 * getSquare(radius)
getShapeArea = lambda height,width: height * width 


radius = 10
height = 5
width = 8
print(getCircleArea(10))
print(getShapeArea(height,width))
