#concept of list
memories = ['Movies','Friends',1250000,True,12.07]
print(memories)
print(memories[0]) # movies
print(memories[1:3]) # friends 1250000
print(memories[3:])
print(memories * 3)
fruits = ['banana','mango','pinapple','apple','orange']
print(fruits)
new_list = fruits + memories
print(new_list)
memories[0] = "Book"
print(memories)
del memories[0]
print(memories)
