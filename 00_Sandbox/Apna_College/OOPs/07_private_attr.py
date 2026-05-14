# Private attributes & methods are meant to be used only within the class and are not
# accessible from outside the class but can work internally in the class

class Account:

    __name = "Anonymous"

    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   # Private attribute

    def reset_pass(self):
        print(self.__acc_pass)   # in class it will work but not outside

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
#print(acc1.acc_pass)  # This need to be private means should not be accessed from out side the class hence not work
print(acc1.reset_pass())   #this will work
print(acc1.__name)