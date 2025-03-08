#string related functions
name = "The Easylearn Academy"
amount = "1234567890"
address = "105evasurbhioppakshwarwadi"
alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
countries = ['India','USA','UK','Australia','Brazil']
print(name.lower())
print(name.upper())
print(len(name))
print(len(countries))
print(name.isupper())
print(name.islower())
print(address.isalnum())
print(amount.isnumeric())
print(name.isspace())
print(alphabets)
list = alphabets.split()
print(list)
countriess = ' '
print(countriess.join(countries))