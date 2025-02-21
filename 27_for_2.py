#write a program to count no of vowels in string given by user
name = input("What is your name") # ankit 
count=0
vowels = ['a','e','i','o','u']
for letter in name:
    letter = letter.lower()
    # if letter=='a' or letter=='i' or letter=='e' or letter=='o' or letter=='u':
    if letter in vowels:
        count+=1
print(f"count of vowel = {count}")
