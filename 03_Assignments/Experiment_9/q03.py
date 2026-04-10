# 1. Single Inheritance
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

# 2. Multiple Inheritance
class Father:
    def skill(self):
        return "Programming"

class Mother:
    def hobby(self):
        return "Painting"

class Child(Father, Mother):
    def display(self):
        return f"{self.skill()} and {self.hobby()}"

# 3. Multilevel Inheritance
class Grandparent:
    def legacy(self):
        return "Antique Watch"

class Parent(Grandparent):
    def house(self):
        return "Suburban Home"

class GrandChild(Parent):
    def bike(self):
        return "Mountain Bike"

# 4. Hierarchical Inheritance
class Vehicle:
    def info(self):
        return "Transportation"

class Car(Vehicle):
    def drive(self):
        return "Driving on road"

class Plane(Vehicle):
    def fly(self):
        return "Flying in air"

# 5. Hybrid Inheritance
class Base:
    def top(self):
        return "Top Level"

class LevelA(Base):
    def middle_a(self):
        return "Middle A"

class LevelB:
    def middle_b(self):
        return "Middle B"

class Bottom(LevelA, LevelB):
    def end(self):
        return "Bottom Level"

# Executing tests
if __name__ == "__main__":
    d = Dog()
    c = Child()
    gc = GrandChild()
    p = Plane()
    b = Bottom()
    
    print(f"Single: {d.speak()} {d.bark()}")
    print(f"Multiple: {c.display()}")
    print(f"Multilevel: {gc.legacy()}, {gc.house()}, {gc.bike()}")
    print(f"Hierarchical: {p.info()}, {p.fly()}")
    print(f"Hybrid: {b.top()}, {b.middle_a()}, {b.middle_b()}, {b.end()}")