#tuples concept
gods = ('shiv','bramha','vishnu')
devtas = ('ganesh','kartik','hanuman')
print(gods)
print(devtas)
print("count of shiv " + str(gods.count('shiv')))
print("count of ram " + str(gods.count('ram')))
print("position of vishnu " + str(gods.index('vishnu')))
# position = gods.index('ram') #since ram is not in tuple it will generate key error and code will stop 
# print(position)
print('good bye')