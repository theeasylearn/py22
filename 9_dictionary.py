#concept of dictionary
# person = ['Gorbachav','Mikhile',True,40,True]
# person = {'name':"Ankit",'surname':"Patel",'age':38,'gender':True,'secret':None}
# print(person)
# print(person['name'])
# person['name'] = "ANKIT"
# del person['secret']
# print(person)

book = {}
book['name'] = 'Atomic Habit'
book['price'] = 1000
book['author'] = "James clear"
#add tuples into dictionary
book['chapters'] = (1,2,3,4)
#add list into dictionary 
book['topics'] = ['Energy','focus','hard work']
print(book)

movies = []
movie1 = {'name':'abc','year':2023}
movie2 = {'name':'ghi','year':2024}
movie3 = {'name':'xyz','year':2025}
#add dictionary into list
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)