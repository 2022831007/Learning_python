class Car:
    def __init__(self,type):
        self.type=type
    color="black"
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car Stopped.")    


class VMW(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

# car1 = VMW("fourtuner")
# car2 = VMW("prius")
# print(car1.name)
# print(car1.start())

# print(car2.stop())
# print(car1.color)
car1 = VMW("prious","electric")
print(car1.type)


