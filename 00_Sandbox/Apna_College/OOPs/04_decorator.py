# STATIC METHODS
# Methods that dom't use the self parameter(work at class level)


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    @staticmethod   # decorator
    def hello():
        print("Hello!")

    def average(self):
        i=0
        for i in self.marks:
            i+=i
        print("Hii", self.name, "Your avg score is ",i/3)

s1 = Student('Arpit',[98, 56, 95])
s1.average()
s1.hello()