class Student:

    #default Constructor 
    def __init__(self):
        pass

    # parametarized constructor  (constructors containing parameters other than SELF)
    def __init__(self, name,marks):   # self parameter must be passed othe wise it will show error
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

s1 = Student("Karan", 96)
print(s1.name)
print(s1.marks)

s2 = Student("arjun", 98)
print(s2.name, s2.marks)