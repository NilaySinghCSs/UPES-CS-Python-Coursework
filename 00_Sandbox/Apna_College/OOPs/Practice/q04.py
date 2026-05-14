class Employee:
    def __init__(self,role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
         print("Role = ", self.role)
         print("Dept = ", self.dept)
         print("Salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

    def showDetails2(self):
        print("Name = ",self.name)
        print("Age = ",self.age)


engg1 = Engineer("Musk", 40)
engg1.showDetails2()
engg1.showDetails()
