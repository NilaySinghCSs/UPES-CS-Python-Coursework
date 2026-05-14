# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)      # Rahul kuamr
# print(Person.name)  # Anonymous


# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         Person.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)      # Rahul kuamr
# print(Person.name)  # Rahul kumar

class Person:
    name = "Anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Rahul"

    @classmethod  #decorator
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)      # Rahul Kumar
print(Person.name)  # Rahul Kumar