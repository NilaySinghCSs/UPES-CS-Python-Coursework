# class Student:
#     def __init__(self,phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

#     def calPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)   # 98.0%

# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage)    # 98.0% (percentage not changed on changing physics marks)
# stu1.calPercentage()
# print(stu1.percentage)    # 94.0%


class Student:
    def __init__(self,phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


stu1 = Student(98, 97, 99)
print(stu1.percentage)   

stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)    
