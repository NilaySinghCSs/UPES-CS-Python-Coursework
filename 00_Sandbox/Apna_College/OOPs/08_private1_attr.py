class Person:
    __name = "Anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())