# print("noman")


# class Bird:
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("most birds can fly,but some cannot.")

# class sparrow(Bird):
#     def flight(self):
#         print("sparrow can fly.")
    
# class ostrich(Bird):
#     print("ostirch cannot fly.")
# bird1 = sparrow()
# bird2 = ostrich()

# bird1.intro()
# bird1.flight()
# bird2.intro()
# # bird2.flight()

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def _init_(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Square(Shape):
#     def _init_(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side * self.side

# circle = Circle(5)
# square = Square(4)

# print("Circle area:", circle.area())
# print("Square area:", square.area())

# if 5 > 2:


# k = 35.82
# k = str(k)
# print(k)

# k = 35
# k = float(k)
# print(k)

# k = 35
# k = str(k)
# print(k)


# w = 'Noman'
# print(w[3])

# h = 'college'
# print(h[5])





# txt = 'Noman is learning Advance python'
# if 'Hamza' in txt:
#     print("Yes This exists in txt")
# # else:
# #     print("It DOesnt Exist in txt")



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
    

# class dog(Animal):
#     def make_sound(self):
#         return "woof,woof!"

# class cat(Animal):
#     def make_sound(self):
#          return "meow,meow!"
    
# dog = dog()
# cat = cat()
# print(dog.make_sound())
# print(cat.make_sound())


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area())


# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area (self):
#         pass

# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class square(shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side
# circle = circle(5)
# shape = shape(4)
# print("circle area:", circle.area())
# print("square.area:", square.area())


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area())

