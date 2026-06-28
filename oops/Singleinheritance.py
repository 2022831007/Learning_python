class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car Stopped.")    


class VMW(Car):
    def __init__(self,name):
        self.name=name

car1 = VMW("fourtuner")
car2 = VMW("prius")
print(car1.name)
print(car1.start())

print(car2.stop())
print(car1.color)


