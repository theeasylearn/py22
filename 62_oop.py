class person:
    def walk(self):
        print("i can walk....")
        
    def talk(self):
        print("i can talk....")
        
    def details(self,name,age,mobile):
        print("name : ",name)
        print("age : ",age)
        print("mobile : ",mobile)
        
        
        
# object -> instance -> self
      
# obj_name = class_name()

# creating object
p1 = person()

# walk()
# calling method of class
p1.walk()
p1.talk()


p2 = person()
p2.details("raj",23,1234567890)

p3 = person()
p3.details("ram",30,1234567890)

