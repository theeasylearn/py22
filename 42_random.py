import random 
#random float number between 0.0 and 1.0 
number = random.random()
print("random float number between 0.0 and 1.0 ",number)
#random float number between 10 and 99
number = random.uniform(10,99)
print("random float number between 10 and 99 ",number)

#random integer number between 10 and 99
number = random.randint(10,99)
print("random integer number between 10 and 99 ",number)

#random integer number between 10 and 99 and with gap of 20
number = random.randrange(10,99,20)
print("random integer number between 10 and 99 with gap of 20",number)

states = ['Gujarat','Maharastra','Rajasthan','Madhya Pradesh','punjab']
print(states)
#randomly pick one state 
print("any one random state ",random.choice(states))

#randomly pick 2 state 
print("any one random state ",random.choices(states,k=2))

#shake list values 
random(states)
print(states)