#import module from package 
from world.asia import country as a
from world.europe import country as e
from world import continent
#use module 
list = a.getCountries()
print(list)

list2 = e.getCountries()
print(list2)

list3 = continent.getContinent()
print(list3)

