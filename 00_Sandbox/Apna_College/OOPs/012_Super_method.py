# SUPER METHOD is used to access methods of the parent class.

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self,name, type):
        self.name = name
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar('Prius', "electric")
print(car1.type)
