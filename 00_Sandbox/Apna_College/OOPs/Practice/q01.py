# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        i=0
        for i in self.marks:
            i+=i
        print("Hii", self.name, "Your avg score is ",i/3)

s1 = Student('Arpit',[98, 56, 95])
s1.average()

s1.name = "ironman"
s1.average()
