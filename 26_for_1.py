#concept of for loop 
numbers = [100,25,50,75,60,45,20,99,77]
print(numbers)
#findout sum of above list 
sum = 0
for num in numbers:
    print(num,end= ' ')
    sum+=num # sum = sum + num 
print() #for new line
print(f"sum = {sum}")

#count odd & even value
odd = 0 #5
even = 0 #4
for num in numbers:
    reminder = num % 2 # 0
    if reminder==0: 
        even+=1
    else:
        odd+=1

print(f"even  = {even} odd = {odd}")

books = ('abc','xyz','ghi','ert','yui')
print(books)

name = input("What is book name") #xyz
is_found = False; #we assume book not found
for item in reversed(books):
    if item==name:
        print("book found in tuple")
        is_found = True
        break #break (stop ) loop
    
if not is_found:
    print("book not found in list")