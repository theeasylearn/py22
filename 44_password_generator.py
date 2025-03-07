import password
pwd1 = password.GeneratePassword() #generate password of 12 length
pwd2 = password.GeneratePassword(20) #generate password of 20 length
pwd3 = password.GeneratePassword(length=30) #generate password of 30 length
pwd4 = password.GeneratePassword(length=-40) #generate password of 40 length
pwd5 = password.GeneratePassword(length=50) #generate password of 50 length

print("12 length password = ",pwd1)
print("20 length password = ",pwd2)
print("30 length password = ",pwd3)
print("40 length password = ",pwd4)
print("50 length password = ",pwd5)