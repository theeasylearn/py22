#concept of in and not in operator 
fruits = ['banana','mango','pineapple','kiwi','orange']
print(fruits)
favorite_fruit = input("Enter your favorite fruit name") #apple
isFound = favorite_fruit in fruits
print(isFound)

isNotFound = favorite_fruit not in fruits
print(isNotFound)

cities = "Bhavnagar Baroda Rajkot Surendranagar"
print(cities)
current_city = input("where do you live (city)?")
isFound = current_city in cities
print(isFound)
