#concept of set 
fruits = {'graps','kiwi','orange'}
print(fruits)
fruits.add('apple')
fruits.add('kiwi')
fruits.add('graps')
print(fruits)
fruits.remove('kiwi')
print(fruits)

set1 = {1,5,8,11}
set2 = {8,11,25,45}
print(set1,set2)

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(union)
print(intersection)
print(difference)