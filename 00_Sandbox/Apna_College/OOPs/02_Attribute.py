class Student:
    college_name = "ABC College"
    name = "Anonymous"  # classs attr

    def __init__(self, name,marks):   # self parameter must be passed othe wise it will show error
        self.name = name   # object attr
        self.marks = marks
        print("Adding new student in Database..")

# object attr > class attr (priority given)  [Generally we keep different name of class and object attributes]

s1 = Student("arjun", 98)
print(s1.name, s1.marks)