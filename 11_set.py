#concept of set 
fruits = {'Apple','Banana','Mango','kiwi','graps'}
print(fruits)
fruits.add('Apple')
fruits.add('coconut')
fruits.remove('Apple')
print(fruits)

set1 = {1,2,3}
set2 = {2,3,4}
print(set1,set2)
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(union)
print(intersection)
print(difference)
