class person:
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")
        
class student(person):
    def read(self):
        print("i can read")
        
    def write(self):
        print("i can write")
        
class employee(person):
    def __init__(self,id,office_code):
        super().__init__()
        self.id=id
        self.office_code=office_code
    
    def show_info(self):
        print("id : ",self.id)
        print("office code : ",self.office_code)
        
        
obj = employee(101,"ofc07")
obj.show_info()
obj.walk()
obj.talk()

obj2 = student()
obj2.read()
obj2.write()
obj2.walk()
obj2.talk()
