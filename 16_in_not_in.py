#concept of in and not in operator 
fruits = ['banana','mango','pinapple','kiwi','orange']
print(fruits)
favorite_fruit = input("Enter your favorite fruit name") #apple
is_found = favorite_fruit in fruits
print(is_found)

is_not_found = favorite_fruit not in fruits
print(is_not_found)