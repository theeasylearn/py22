#dictionary methods 
person = {'name':"Ankit",'surname':"Patel",'age':38,'gender':True,'secret':123123}
print(person)
# get only keys 
keys = person.keys();
values = person.values();
items = person.items();
print(keys)
print(values)
print(items)
person2 = dict.fromkeys(person) #create new dictionary which should have name,surname age, gender secret with None as value
print(person2)
person2.update({'name':'pramit','surname':'kanzariya','age':19,'email':'abc@gmail.com'})
print(person2)

#let pop email from person2
email = person2.pop('email',None)
print(email)
removed_item = person2.popitem()
print(removed_item)

person3 = person2 #this will create reference of person2 in person3 means both are same
person2.clear()
print(person2)
print(person3)
person4 = person.copy() #this will create shallow copy. change one will not effect other dictionary
print('before change ')
print(person)
print(person4)
person.popitem()
person4['address'] = 'Hill drive, bhavnagar'
print('after change')
print(person)
print(person4)
