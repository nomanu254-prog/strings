# # Base class
# class vehicle:
#     def __init__(self,speed,color):
#         self.speed = speed
#         self.color = color
#     def drive (self):
#         print("driving a vehicle....")

# # derived class car
# class car(vehicle):
#     def drive (self):
#         print(f"The {self.color} car is zooming at {self.speed} km/h.")
# # derived class bike
# class bike(vehicle):
#     def drive (self):
#         print(f"The {self.color} bike is zooming at {self.speed} km/h.")
# # polymorphism demonstration
# vehicles = [
#     car(120,"red"),
#     bike(80,"blue"),
#     car(150,"black"),
#     car(350,"Metallic Grey")
# ]
# for vehicle in vehicles:
#     vehicle.drive()

# # Student class
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# # List of students
# students = [
#     Student("Alice", 20),
# #     Student("Bob", 22),
# #     Student("Charlie", 19)
# # ]

# # # Printing each student's introduction
# # for student in students:
# #     student.introduce()


# # class students:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #     def introduce(self):
# #         print(f"Hi, I'm {self.name} and I'm{self.age} years old.")

# # students = [
# #     students("alice",20),
# #     students("bob",30),
# #     students("peter",50)
# #     ]
# # for student in students:
# #     student.introduce()

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
# bird2.flight()


 

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("most birds can fly,but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("sparrow can fly.")
    
class ostrich(Bird):
    print("ostirch cannot fly.")
bird1 = sparrow()
bird2 = ostrich()

bird1.intro()
bird1.flight()
bird2.intro()
bird2.flight()

print("noman")