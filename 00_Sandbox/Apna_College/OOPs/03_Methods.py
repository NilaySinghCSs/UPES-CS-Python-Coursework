class Student:
    college_name = "ABC College"
    

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):    # self parameter is necessary either we are using inside the method or not
        print("Welcome Student", self.name)

    def get_marks(self):
        return self.marks
        

s1 = Student("arjun", 98)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())