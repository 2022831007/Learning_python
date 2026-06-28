class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car Stopped.")    


class VMW(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(VMW):
    def __init__(self,type):
      self.type=type  


car1 = Fortuner("disel") 
car1.start()     



