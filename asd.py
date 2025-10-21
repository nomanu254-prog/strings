from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def _init_(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area())