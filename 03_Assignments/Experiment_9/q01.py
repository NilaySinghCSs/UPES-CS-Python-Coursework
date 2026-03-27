class Student:
    def __init__(self):
        self.name = ""
        self.sap_id = ""
        self.marks = []

    def take_input(self):
        self.name = input("Enter Student Name: ")
        self.sap_id = input("Enter SAP ID: ")
        
        print(f"Enter marks for {self.name}:")
        phy = float(input("  Physics: "))
        chem = float(input("  Chemistry: "))
        maths = float(input("  Maths: "))
        
        self.marks = [phy, chem, maths]

    def display_details(self):
        print(f"Name: {self.name} | SAP ID: {self.sap_id}")
        print(f"Marks -> Physics: {self.marks[0]} | Chemistry: {self.marks[1]} | Maths: {self.marks[2]}")
        print("-" * 45)

students = []
for i in range(3):
    print(f"\n--- Entering details for Student {i+1} ---")
    student = Student()
    student.take_input()
    students.append(student)
print("\n" + "="*12 + " ALL STUDENT DETAILS " + "="*12)
for student in students:
    student.display_details()