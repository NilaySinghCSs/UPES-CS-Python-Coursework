#             SINGLE INHERITANCE 

class Car:
    Color = "Bkack"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("BMW")

print(car1.Color)
print(car1.name)
print(car1.start())