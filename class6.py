
# # class students:
# #    def __init__(self,name,age,father_name):
# #       self.name = name
# #       self.__age = age
# #       self.__father_name = father_name
   
# #    def get_father_name(self):
# #       return self.__father_name
# #    def get_age(self):
# #       return self.__age
# # st1 = students("noman",25,'fareed_ullah_khan')
# # print(st1.name)
# # print(st1.get_age())
# # print(st1.get_father_name())

# # class BankAccount:
# #    def __init__(self,balance):
# #       self.__balance = balance
# #    def deposit(self,amount):
# #          if amount > 0:
# #             self.__balance +=amount
# #    def get_balance(self):
# #          password = input("Enter your Password:")
# #          if password == "noman123":
# #              return self.__balance
# #          else:
# #              print("Unauthorized accessed !")
# # acc = BankAccount(1000)
# # acc.deposit(500)
# # print(acc.get_balance())

# class BankAccount:
#     def __init__(self,balance):
#       self.__balance = balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance +=amount
#     def get_balance(self):
#         password = input("Enter your password:")
#         if password == "noman123":
#             return self.__balance
#         else:
# #             print("unauthorized accessed !")
# # acc = BankAccount(1000)     
# # acc.deposit(5000)      
# # print(acc.get_balance())

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self,amount):
#         if amount > 0:
#             self .__balance +=amount
#     def get_balance(self):
#         password = input("Enter your password:")
#         if password =="noman12345":
#             return self.__balance
#         else:
#             print("unauthorized accessed!")
# acc = BankAccount(1000)
# acc.deposit(12000)
# print(acc.get_balance())

# Base class
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def turn_on(self):
        print(f"{self.brand} Laptop is starting...")

# Derived class
class GamingLaptop(Laptop):
    def __init__(self, brand, ram, gpu):
        super().__init__(brand, ram)
        self.gpu = gpu

    def show_specs(self):
        print(f"Gaming Laptop Specs:\nBrand: {self.brand}, RAM: {self.ram}GB, GPU: {self.gpu}")

# Testing the classes
laptop1 = Laptop("Dell", 8)
laptop1.turn_on()

gaming_laptop1 = GamingLaptop("Asus", 16, "NVIDIA RTX 3080")
gaming_laptop2 = GamingLaptop("Alienware", 64, "NVIDIA RTX 5090")
gaming_laptop1.turn_on()
gaming_laptop1.show_specs()
gaming_laptop2.turn_on()
gaming_laptop2.show_specs()


    
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def turn_on(self):
        print(f"{self.brand} Laptop is starting...")

class GamingLaptop(Laptop):
    def __init__(self, brand, ram, gpu):
        super().__init__(brand, ram)
        self.gpu = gpu

    def show_specs(self):
        print(f"Gaming Laptop Specs:\nBrand: {self.brand}, RAM: {self.ram}GB, GPU: {self.gpu}")
laptop1 = Laptop("Dell", 8)
laptop1.turn_on()
gaming_laptop1 = GamingLaptop("Asus", 16, "NVIDIA RTX 3080")
gaming_laptop2 = GamingLaptop("Alienware", 64, "NVIDIA RTX 5090")
gaming_laptop1.turn_on()
gaming_laptop1.show_specs()
gaming_laptop2.turn_on()
gaming_laptop2.show_specs()

# Base class
class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print("Driving a vehicle...")

# Derived class Car
class Car(Vehicle):
    def drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")

# Derived class Bike
class Bike(Vehicle):
    def drive(self):
        print(f"The {self.color} bike is zooming at {self.speed} km/h.")

# Polymorphism demonstration
vehicles = [
    Car(120, "red"),
    Bike(80, "blue"),
    Car(150, "black")
]

for vehicle in vehicles:
    vehicle.drive()  # Each object uses its own version of drive()

print("noman")



