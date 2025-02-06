#concept of dictionary
person = ['Gorbachav','Mikhile',True,40,True]
person = {'name':"Ankit",'surname':"Patel",'age':38,'gender':True,'secret':None}
print(person)
print(person['name'])
person['name'] = "ANKIT"
del person['secret']
print(person)

books = {} #empty dictionary
books['name'] = "The Atomic habit"
books['author'] = "James clear"
books['chapters'] = (1,2,3,4,5)
books['topics'] = ['index','preface','introduction']
print(books)
#ger first chapter 
print(books['chapters'][0])
#get second topic 
print(books['topics'][1])
movies = [] #empty list
movies.append({'name':'abc','year':2025}) #add dictionary into list
movies.append({'name':'xyz','year':2026}) #add dictionary into list
movies.append({'name':'pqr','year':2027}) #add dictionary into list
print(movies)