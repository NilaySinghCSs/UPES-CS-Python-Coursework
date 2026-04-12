class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(10, 20)
p2 = Point(12, 15)
p3 = p1 + p2

print(f"P1: {p1}")
print(f"P2: {p2}")
print(f"P3: {p3}")