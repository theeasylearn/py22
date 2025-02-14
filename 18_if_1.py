#concept of simple decision making if 
#write a program to findout area of shape using given(input will be given by user) length and width
'''
    take length and width from user 
    check length and width are positive or not. if not convert it into positive
    calculate area using formula area = length * width 
    display area 
'''
length = int(input("Enter length of the shape")) # -20
width = int(input("Enter width of the shape"))

if length<0: # == != < > <= >=
    #convert negative into positive
    length = 0 - length

if width<0: # == != < > <= >=
    #convert negative into positive 
    width = 0 - width

area = length * width
print("area " + str(area))