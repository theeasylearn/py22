class vehicles:
    def __init__(self,speed,seats):
        self.speed = speed
        self.seats = seats
        
    def show_info(self):
        print("speed : ",self.speed)
        print("seats : ",self.seats)
        
class car(vehicles):
    def __init__(self, speed, seats,color):
        super().__init__(speed, seats)
        self.color = color
        
    def car_info(self):
        print("color : ",self.color)
        
class sports_car(car):
    def __init__(self, speed, seats, color,hoursepower):
        super().__init__(speed, seats, color)
        self.hourse_power = hoursepower
        
    def sports_car_info(self):
        print("hourse power : ",self.hourse_power)
      
  
obj = sports_car(8,4,"black",9.5)
obj.sports_car_info()
obj.car_info()
obj.show_info()