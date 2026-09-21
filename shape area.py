class Shape:
    def area(self):
        pass

class Circle(Shape):
    pi = 3.14
    r = int(input("Enter r: "))
    def area(self):
        return self.pi * self.r * self.r

class Rectangle(Shape):
    l = int(input("Enter l: "))
    b = int(input("Enter b: "))
    def area(self):
        return self.l * self.b

class Triangle(Shape):
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    def area(self):
        return 0.5 * self.b * self.h

c = Circle()
r = Rectangle()
t = Triangle()

print("Area of Circle: ", c.area())
print("Area of Rectangle: ", r.area())
print("Area of Triangle: ", t.area())
