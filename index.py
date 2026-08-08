# class

# class Car:
#     print("hello how are you")

# class Car:
#     a = 10 #attribute

#     def hello(): #method
#         print("hello how are you")

# print(Car.a)
# Car.hello()


# objects

# class Bags:
#     name = "Gucci"
#     def details(self):
#         print("This is a Gucci bag")

# reebok = Bags() # creating an object (reebok) of class Bags
# campus = Bags() # creating an object (campus) of class Bags

# campus.name = "Campus" # changing the attribute name of object campus

# print(campus.name) # printing the attribute name of object campus
# reebok.details() # calling the method details() using the object reebok


# consttructor

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Suman", 23)
# s2 = Student("Ramesh", 25)

# print(s1.name)
# print(s2.age)

# class Bags:
#     def __init__(self, material, zips, color, pockets):
#         self.material = material
#         self.zips = zips
#         self.color = color
#         self.pockets = pockets

# reebok = Bags("leather", 2, "black", 3)
# print(reebok.material, reebok.zips, reebok.color, reebok.pockets)

# campus = Bags("canvas", 1, "blue", 2)
# print(campus.material, campus.zips, campus.color, campus.pockets)


# Types of Atributes and methods

# class Animal:
#     a = 10 # class attribute

#     def __init__(self, name, age):
#         self.name = name # instance attribute
#         self.age = age # instance attribute

#     def details(self): # instance method
#         print(f"Name: {self.name}, Age: {self.age}") 

#     @classmethod
#     def hello(cls):
#         print("Hello, I am an animal") # class method

#     @staticmethod
#     def info():
#         print("Animals are multicellular eukaryotic organisms") # static method    

# obj = Animal("Dog", 5)

# print(obj.a) # accessing class attribute using object
# print(obj.name) # accessing instance attribute using object
# print(obj.age) # accessing instance attribute using object

# obj.details() # calling instance method using object


# Inhertiance

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def details(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class Human(Animal):
#     pass

# obj = Animal("Dog", 5)
# obj2 = Human("John", 30)

# obj.details() # calling method of parent class using object of parent class
# obj2.details() # calling method of parent class using object of child class


# constructor in inheritance

# class bagFactory:
#     def __init__(self, material, pockets, zips):
#         self.material = material
#         self.pockets = pockets
#         self.zips = zips

#     def display(self):
#         print(f"Material: {self.material}, Pockets: {self.pockets}, Zips: {self.zips}")

# class Reebok(bagFactory):
#     def __init__(self, material, pockets, zips, color):
#         super().__init__(material, pockets, zips) # calling constructor of parent class
#         self.color = color # adding a new attribute specific to the Reebok class

#     def display(self):
#         super().display() # calling the display method of the parent class
#         print(f"Color: {self.color}")

# bag1 = bagFactory("Leather", 3, 2)
# bag2 = Reebok("Canvas", 2, 1, "Red")

# bag1.display() # calling display method of bagFactory class
# bag2.display() # calling display method of Reebok class


# Polymorphism

# def hello():
#     print("Hello, I am a function")

# def hello():
#     print("Hello, I am another function with the same name")

# hello() # calling the second hello function, which overrides the first one

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# obj = Animal()
# obj2 = Dog()

# obj.sound() # calling the sound method of Animal class
# obj2.sound() # calling the sound method of Dog class, which overrides the sound method of Animal class

# Method Overloading

# class Calculator:
#     def add (self, a, b):
#         return a + b

#     def add (self, a,b,c = None):
#         if c is not None:
#             return a + b + c
#         else:
#             return a + b 

# calc = Calculator()
# print(calc.add(2, 3)) # calling the add method with 2 arguments
# print(calc.add(2, 3, 4)) # calling the add method with 3 arguments


# Method Overriding

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# obj = Dog()
# obj.sound() # calling the sound method of Dog class, which overrides the sound method of Animal class


# Encapsulation

# class BankAccount:
#     def __init__(self, account, balance):
#         self.account = account
#         self.__balance = balance # private attribute

#     def display_account_info(self):
#         print("Account:", self.account)

#     def deposit(self, amount):
#         self.__balance += amount # modifying private attribute

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount # modifying private attribute
#         else:
#             print("Insufficient balance")
    
#     def get_balance(self):
#         return self.__balance # accessing private attribute


# account = BankAccount("123456789", 1000)
# account.display_account_info() # calling public method to display account info
# account.deposit(500) # calling public method to deposit money
# account.withdraw(200) # calling public method to withdraw money
# print(account.get_balance()) # calling public method to get balance


# Abstraction

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

# obj=Car()
# obj.start() # calling the start method of Car class
# obj.stop() # calling the stop method of Car class

# obj2=Vehicle() # trying to create an object of abstract class Vehicle will raise an error


# Dunder Methods

# class Student:
#     def __init__(self, name, id):       # constructor or __init__ method
#         self.name = name
#         self.id = id

#     def __str__(self):                  # dunder method to return a string representation of the object
#         return f"Student Name: {self.name}, Student ID: {self.id}"

# s1 = Student("Suman", 23)
# print(s1) # calling the __str__ method of Student class

# class Book:
#     def __init__(self,length):
#         self.length = length

#     def __len__(self):                  # dunder method to return the length of the object
#         return self.length
    
# b1 = Book(100)
# print(len(b1)) # calling the __len__ method of Book class


# decorators

# def deco_greet(func):
#     def wrapper():      # inner function that wraps the original function
#         print("Before calling the function")
#         func()          # calling the original function
#         print("After calling the function")
#     return wrapper

# @deco_greet     # applying the decorator to the greet function
# def greet():
#     print("Hello, welcome to the world of Python!")

# greet() # calling the decorated greet function


# *args and **kwargs

# def add_numbers(*args): # *args allows for a variable number of positional arguments

#     print("Arguments received:", args) # printing the arguments received

#     total = 0
#     for num in args:
#         total += num
#     return total

# print(add_numbers(1, 2, 3, 4, 5)) # calling the add_numbers function with multiple arguments

# def print_info(**kwargs): # **kwargs allows for a variable number of keyword arguments
    
#     print("Keyword arguments received:", kwargs) # printing the keyword arguments received

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
    
# print_info(name="Suman", age=23, city="Kathmandu") # calling the print_info function with multiple keyword arguments


# ternary operator

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# b = [i for i in a if i % 2==0]


# print(b) # printing the list b which contains even numbers from list a and double of odd numbers from list a


# Lambda function

# check = lambda x: "even number" if x%2==0 else "odd number" # lambda function to check if a number is even or odd

# print(check(10)) # calling the lambda function with an even number
# print(check(11)) # calling the lambda function with an odd number

# addition = lambda a,b : a + b

# print(addition(12,21)) # calling the lambda function to calculate the addition of two numbers

# square = lambda x : x*x

# print(square(5)) # calling the lambda function to calculate the square of a number


# map, filter and zip

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x : x*x, numbers)) # using map to apply a lambda function to each element of the list

print(squared_numbers) # printing the list of squared numbers

even_numbers = list(filter(lambda x : x%2 == 0, numbers)) # using filter to appy lambda function to each element of the list to check the even number

print(even_numbers)

names = ["Suman", "Rahul", "Amit"]
marks = [100 , 80 , 90]

results = list(zip(names, marks))

print(results)
