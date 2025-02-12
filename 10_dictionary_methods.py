#dictionary methods 
school = {'name':'bright school','city':'bhavanagar','year':2000}
print(school)

school2 = school.copy() #shallow copy 
school2.clear()
print(school,school2)

new_school = dict.fromkeys(school)
print(new_school)

keys = school.keys()
values = school.values()
items = school.items()

print(keys)
print(values)
print(items)

removed_item = school.pop('year')
print(removed_item)
removed_item = school.popitem()
print(removed_item)
print(school.get('name'))
print(school.get('email'))
print(school.update({'email':'abc@gmail.com'}))
print(school.update({'name':'sunstar'}))
print(school)