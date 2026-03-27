class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = [phy, chem, maths]

    def display(self):
        print(f"Name: {self.name} | SAP ID: {self.sap_id}")
        print(f"Marks -> Physics: {self.marks[0]} | Chemistry: {self.marks[1]} | Maths: {self.marks[2]}")

    def find_marks_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / 300) * 100
        return round(percentage, 2)

    def display_result(self):
        if all(mark > 40 for mark in self.marks):
            return "Pass"
        else:
            return "Fail"

def find_class_average(student_list):
    if not student_list:
        return 0.0
    
    total_percentage = sum(student.find_marks_percentage() for student in student_list)
    class_average = total_percentage / len(student_list)
    return round(class_average, 2)

students = []
n = int(input("Enter the number of students: "))

for i in range(n):
    print(f"\n--- Entering details for Student {i+1} ---")
    name = input("Enter Name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks (out of 100): "))
    chem = float(input("Enter Chemistry marks (out of 100): "))
    maths = float(input("Enter Maths marks (out of 100): "))
    
    student_obj = Student(name, sap_id, phy, chem, maths)
    students.append(student_obj)

print("\n" + "="*15 + " FINAL REPORT " + "="*15)
for student in students:
    student.display()
    print(f"Percentage: {student.find_marks_percentage()}%")
    print(f"Result: {student.display_result()}")
    print("-" * 45)

average = find_class_average(students)
print(f"\n=> Overall Class Average Percentage: {average}%")