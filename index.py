# class Car:
#     print("hello how are you")

# class Car:
#     a = 10 #attribute

#     def hello(): #method
#         print("hello how are you")

# print(Car.a)
# Car.hello()

# objects
class Bags:
    name = "Gucci"
    def details(self):
        print("This is a Gucci bag")

reebok = Bags() # creating an object (reebok) of class Bags
campus = Bags() # creating an object (campus) of class Bags

campus.name = "Campus" # changing the attribute name of object campus

print(campus.name) # printing the attribute name of object campus
reebok.details() # calling the method details() using the object reebok
