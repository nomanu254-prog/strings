# # # # class Car:
# # # #     def __init__(self, brand, model):
# # # #         self.brand = brand
# # # #         self.model = model
    
# # # #     def drive(self):
# # # #         print(f"{self.brand} {self.model} is driving....")


# # # # car1 = Car("Toyota", "Corolla")
# # # # car2 = Car("Honda","Civic")

# # # # car1.drive()
# # # # car2.drive()


# # # class students:
# # #     def __init__(self,name,age,roll_no):
# # #         self.name = name
# # #         self.age = age
# # #         self.roll_no = roll_no
# # # s1 = students('hamza',25,22)
# # # print(s1.name)
# # # s2 = students('shakir',35,22)
# # # s3 = students('hashir',26,24)
# # # s4 = students('bilal',37,28)
# # # print(s2.name,s1.age,s4.roll_no)
# # # print(s2.name,s2.age,s2.roll_no)
# # # print(s1.name,s1.age,s1.roll_no)

# # # class students:
# # #     def __init__(self,name,age,roll_no):
# # #         self.name = name
# # #         self.age = age
# # #         self.roll_no = roll_no
# # # s1 = students('noman',22,25)
# # # print(s1.name,s1.age,s1.roll_no)
    

# # # class car:
# # #     def __init__(self,brand,model,color):
# # #         self.brand = brand
# # #         self.model = model
# # #         self.color = color
# # # car1 = car('honda',2025,'red')
# # # print(car1.brand,car1.model,car1.color)
# # # car2 = car('civic',2024,'black')

# # class student:
# #     def __init__(self,name,age,roll_no):
# #         self.name = name
# #         self.age = age
# #         self.roll_no = roll_no
# # student1 = student('hashir',10,12)
# # print(student1.name,student1.age,student1.roll_no)

# # class student:
# #     def __init__(self,name,age,roll_no):
# #         self.name = name
# #         self.age = age
# #         self.roll_no = roll_no
# # student1 = student('noman',20,25)
# # # print(student1.name,student1.age,student1.roll_no)

# # # class car:
# # #     def __init__(self,brand,model,color):
# # #         self.brand = brand
# # #         self.model = model
# # #         self.color = color
# # #     def drive(self):
# # #      print(f"{self.brand} {self.model}of color{self.color} is driving")
# # # car1 = car('honda','civic','black')
# # # car1.drive()

# # # class car:
# # #    def __init__(self,brand,model,color):
# # #       self.brand = brand
# # #       self.model = model
# # #       self.color = color
# # #    def drive(self):
# # #       print(f"{self.brand} {self.model} of color{self.color} is driving")
# # # car1 = car('honda','civic','black')
# # # car1.drive()      

# # # class mobile:
# # #    def __init__(self,brand,model,color):
# # #       self.brand = brand
# # #       self.model = model
# # #       self.color = color
# # #    def call(self):
# # #       print(f"{self.brand} {self.model} of color {self.color} is calling")
# # # mobile = mobile('galaxy','S23','blue')
# # # mobile.call()


# # class Animals:
# #    def __init__(self,name):
# #       self.name = name
# #    def speak(self):
# #       print("some Sounds made")

# # class Dog(Animals):
# #    def speak(self):
# #       print(f"{self.name} woof woof!")

# # class Cat(Animals):
# #    def speak(self):
# #       print(f"{self.name} meow meow!")

# # dog = Dog("goldie")
# # cat = Cat("kitty")

# # cat.speak()
# # dog.speak()

# # class animals:
# #    def __init__(self,name):
# #       self.name = name
# #    def speak(self):
# #       print("some sounds made")

# # class dog(animals):
# #    def speak(self):
# #       print(f"{self.name} woof woof!")

# # class cat(animals):
# #    def speak(self):
# #       print(f"{self.name} meow meow!")   

# # dog = dog("goldy") 
# # cat =cat("kitty")

# # cat.speak()
# # dog.speak()

# class students:
#    def __init__(self,name,age,father_name):
#       self.name = name
#       self.__age = age
#       self.__father_name = father_name

#    def get_father_name(self):
#       return self.__father_name

#    def get_age(self):
#       return self.__age
   
# st1 = students("noman",22,'Farid Ullah Khan')
# print(st1.name)
# print(st1.get_age())

class students:
   def __init__(self,name,age,father_name):
      self.name = name
      self.__age = age
      self.__father_name = father_name
   
   def get_father_name(self):
      return self.__father_name
   def get_age(self):
      return self.__age
st1 = students("noman",25,'fareed_ullah_khan')
print(st1.name)
print(st1.get_age())
print(st1.get_father_name())

# class family:
#    def __init__(self,name,age,father_name,):
#       self.name = name
#       self.__age = age
#       self.__father_name = father_name
#    def get_father_name(self):
#       return self.__father_name
#    def get_age(self):
#       return self.__age
# st1 = students("noman",28,'fareed_ullah_khan')
# print(st1.name)
# print(st1.get_age())
# print(st1.get_father_name())
   
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds!")
    
#     def get_balance(self):
#         password = input("Enter password to view balance: ")
#         if password == "secure123":
#             return self.__balance
#         else:
#             return "unauthorized access!"

#     account = BankAccount(10000)
# account.deposit(50000)
# print("Balance:", account.get_balance())


# class Student:
#     def __init__(self, name, age):
#         self.__name = name  # private attribute
# #         self.__age = age    # private attribute
    
#     def get_name(self):
#         return self.__name
    
#     def set_name(self, name):
#         self.__name = name
    
#     def get_age(self):
#         return self.__age
    
# st1 = Student("Hamza", 22)
# print(st1.get_name())
# print(st1.get_age())
# print(st1.set_name("Shakir"))
# print(st1.get_name())

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # Private attribute or Property
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds!")
    
#     def get_balance(self):
#         # simple password protection
#         password = input("Enter PIN to view balance: ")
#         if password == "2200":
#             return self.__balance
#         else:
#             return "Unauthorized access!"

# account = BankAccount(50000)
# print("Balance:", account.get_balance())
# # Try accessing private variable
# print(account.__balance)



# # class BankAccount:
# #     def __init__(self, balance):
# #         self.__balance = balance   # private attribute
    
# #     def deposit(self, amount):
# #         self.__balance += amount
    
# #     def withdraw(self, amount):
# #         if amount <= self.__balance:
# #             self.__balance -= amount
# #         else:
# #             print("Insufficient funds!")
    
# #     def get_balance(self):
# #         # simple password protection
# #         password = input("Enter password to view balance: ")
# #         if password == "secure123":
# #             return self.__balance
# #         else:
# #             return "Unauthorized access!"

# # # Demo
# # account = BankAccount(10000)
# # account.deposit(50000)
# # print("Balance:", account.get_balance())
# # # Try accessing private variable


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private attribute
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("insufficient funds!")

#     def get_balance(self):
#         # simple password protection
#         password = input("Enter password to view balance: ")
#         if password == "secure123":
#             return self.__balance
#         else:
#             return "balance"

# account = BankAccount(20000)
# account.deposit(50000)


class students:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age   
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    st1 = Student("Hamza", 22)
print(st1.get_name())
print(st1.get_age())
print(st1.set_name("Shakir"))
print(st1.get_name())


  
        
