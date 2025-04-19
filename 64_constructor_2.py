class student:
    def __init__(self,name):
        print("constructor called....")
        # create instance variables
        #must use self whenever we create/access/change instance variable
        self.name = name
        self.age = 21
        
    def read(self,language):
        print(self.name + " can read " + language)
        print("my age is " + str(self.age))
    def write(self,language):
        print(self.name + " can write " + language)
        

s1 = student("Pramit")
s1.read("English")
s1.write("Hindi")

