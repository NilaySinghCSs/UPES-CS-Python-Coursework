class Student:

    college_name = "ABC College"   # class attribute

    # init constructor is automatically created whenver we create a object

    def __init__(self, name,marks):   # self parameter must be passed othe wise it will show error
        self.name = name
        self.marks = marks

        # print(self)    # <__main__.Student object at 0x0000025DBB06CC20>
        print("Adding new student in Database..")

s1 = Student("Karan", 96)
print(s1.name)
print(s1.marks)
# print(s1)    # Output:- <__main__.Student object at 0x0000025DBB06CC20>

s2 = Student("arjun", 98)
print(s2.name, s2.marks)

print(s2.college_name)       # ABC College
print(Student.college_name)  # ABC College
