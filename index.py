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

class Animal:
    a = 10 # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute

    def details(self): # instance method
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def hello(cls):
        print("Hello, I am an animal") # class method

    @staticmethod
    def info():
        print("Animals are multicellular eukaryotic organisms") # static method    

obj = Animal("Dog", 5)

print(obj.a) # accessing class attribute using object
print(obj.name) # accessing instance attribute using object
print(obj.age) # accessing instance attribute using object

obj.details() # calling instance method using object


