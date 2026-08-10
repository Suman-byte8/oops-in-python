# OOPS in Python

This repository contains a single Python file, `index.py`, that demonstrates the core concepts of Object-Oriented Programming (OOP) in Python. The examples are commented in the file and cover:

- Classes
- Objects
- Constructors
- Types of attributes and methods
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Dunder methods

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects". Objects are instances of "classes". A class is a blueprint for creating objects that share common structure and behavior.

### Analogy
Think of a class as a blueprint for a house. The blueprint defines the rooms, doors, and windows, but it is not a real house. An object is a real house built from that blueprint. You can build many houses from the same blueprint, and each house can have its own paint color, furniture, and address.

---

## 1. Classes

A class groups related data and functions together. In Python, classes are defined using the `class` keyword.

Example from `index.py`:

```python
class Car:
    a = 10  # attribute

    def hello():  # method
        print("hello how are you")

print(Car.a)
Car.hello()
```

- `class Car:` defines a new class named `Car`.
- `a = 10` is a class attribute.
- `hello()` is a method defined inside the class.

## 2. Objects

Objects are instances of classes. Each object can store its own data and call the class methods.

Example:

```python
class Bags:
    name = "Gucci"

    def details(self):
        print("This is a Gucci bag")

reebok = Bags()
campus = Bags()

campus.name = "Campus"
print(campus.name)
reebok.details()
```

- `reebok = Bags()` creates an object named `reebok` from the `Bags` class.
- `campus.name = "Campus"` changes the `name` attribute for the `campus` object only.
- `reebok.details()` calls the instance method `details()`.

### Analogy
If `Bags` is a recipe for making bags, then `reebok` and `campus` are individual bags created from that recipe.

---

## 3. Constructors

A constructor is a special method named `__init__` that runs when an object is created. It initializes the object's attributes.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Suman", 23)
s2 = Student("Ramesh", 25)

print(s1.name)
print(s2.age)
```

- `__init__` receives `self`, `name`, and `age`.
- `self.name = name` stores values into the object.

Another example with more attributes:

```python
class Bags:
    def __init__(self, material, zips, color, pockets):
        self.material = material
        self.zips = zips
        self.color = color
        self.pockets = pockets

reebok = Bags("leather", 2, "black", 3)
print(reebok.material, reebok.zips, reebok.color, reebok.pockets)
```

### Analogy
A constructor is like moving into a new house and setting the furniture and paint before you start living there.

## 3.1 `*args` and `**kwargs`
Python uses `*args` and `**kwargs` to let functions and methods accept a flexible number of arguments.

- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dictionary.

Example:

```python
class Student:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.extra = args
        self.details = kwargs

s1 = Student("Suman", 23, "A+", country="India", city="Delhi")
print(s1.name)
print(s1.age)
print(s1.extra)
print(s1.details)
```

- `s1.extra` holds the additional positional values: `("A+",)`.
- `s1.details` holds the keyword arguments as a dictionary: `{'country': 'India', 'city': 'Delhi'}`.

This is useful when you want constructors or methods to accept optional or variable data without changing the method signature every time.

---

## 4. Types of Attributes and Methods

In Python, a class can have:

- Class attributes: shared by all instances.
- Instance attributes: unique to each object.
- Instance methods: operate on object data.
- Class methods: operate on the class itself.
- Static methods: utility methods with no access to `self` or `cls`.

Example:

```python
class Animal:
    a = 10  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def details(self):  # instance method
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def hello(cls):
        print("Hello, I am an animal")

    @staticmethod
    def info():
        print("Animals are multicellular eukaryotic organisms")

obj = Animal("Dog", 5)
print(obj.a)
print(obj.name)
print(obj.age)
obj.details()
```

- `a` is a class attribute.
- `self.name` and `self.age` are instance attributes.
- `details()` is an instance method.
- `@classmethod` defines a class method.
- `@staticmethod` defines a static method.

---

## 5. Inheritance

Inheritance allows one class to extend another. The child class inherits attributes and methods from the parent class.

Example:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Human(Animal):
    pass

obj = Animal("Dog", 5)
obj2 = Human("John", 30)
obj.details()
obj2.details()
```

`Human(Animal)` means `Human` inherits from `Animal`.

### Constructor in inheritance

A child class can call the parent constructor using `super()` and then add its own attributes.

Example:

```python
class bagFactory:
    def __init__(self, material, pockets, zips):
        self.material = material
        self.pockets = pockets
        self.zips = zips

    def display(self):
        print(f"Material: {self.material}, Pockets: {self.pockets}, Zips: {self.zips}")

class Reebok(bagFactory):
    def __init__(self, material, pockets, zips, color):
        super().__init__(material, pockets, zips)
        self.color = color

    def display(self):
        super().display()
        print(f"Color: {self.color}")

bag1 = bagFactory("Leather", 3, 2)
bag2 = Reebok("Canvas", 2, 1, "Red")
bag1.display()
bag2.display()
```

- `super().__init__()` calls the parent class constructor.
- `Reebok` extends `bagFactory` and adds `color`.

### Analogy
Inheritance is like a child inheriting traits from a parent. The child shares characteristics but can also have unique features.

---

## 6. Polymorphism

Polymorphism means "many forms". In OOP, the same method name can behave differently depending on the object.

### Example 1: Function override by redefinition

```python
def hello():
    print("Hello, I am a function")

def hello():
    print("Hello, I am another function with the same name")

hello()
```

The second `hello` replaces the first one.

### Example 2: Method overriding in classes

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Animal()
obj2 = Dog()
obj.sound()
obj2.sound()
```

`Dog` overrides `Animal.sound()`.

### Method overloading

Python does not support true method overloading by signature, but you can simulate it with default arguments.

Example:

```python
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))
```

### Method overriding

When a child class provides its own implementation of a parent method:

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()
```

---

## 7. Encapsulation

Encapsulation hides internal object state and only exposes public methods.

Example:

```python
class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.__balance = balance

    def display_account_info(self):
        print("Account:", self.account)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456789", 1000)
account.display_account_info()
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
```

- `__balance` is a private attribute.
- The public methods `deposit`, `withdraw`, and `get_balance` manage access to it.

### Analogy
Encapsulation is like a bank vault: you cannot access the cash directly, only through authorized operations.

---

## 8. Abstraction

Abstraction keeps only the essential details visible and hides complex implementation.

Example using abstract base classes:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

obj = Car()
obj.start()
obj.stop()
```

- `Vehicle` is an abstract class.
- `start` and `stop` are abstract methods that must be implemented by subclasses.

### Analogy
An abstract class is like a contract or requirement list. It says: "Any vehicle must be able to start and stop," but it does not say how.

---

## 9. Dunder Methods

Dunder methods are special methods with double underscores, like `__init__`, `__str__`, and `__len__`. They let objects integrate with Python syntax.

Example:

```python
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.id}"

s1 = Student("Suman", 23)
print(s1)
```

- `__str__` returns a readable string representation of the object.

Another example:

```python
class Book:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

b1 = Book(100)
print(len(b1))
```

- `__len__` allows `len()` to work on custom objects.

---

## How to Use This Project

1. Open `index.py`.
2. Uncomment one example section at a time.
3. Run the file using Python.
4. Observe how class definitions, objects, constructors, and OOP principles work.

## Summary

This project demonstrates the foundational concepts of Python OOP through simple, commented examples. It is a great starting point for learning:

- how to define classes and objects,
- how constructors initialize state,
- how inheritance and polymorphism enable code reuse,
- how encapsulation protects internal data,
- how abstraction defines behavior contracts,
- and how dunder methods make custom classes behave like built-in types.

---

## 10. Decorators
Decorators are a Python feature that lets you modify or enhance functions and methods without changing their code. In the class examples above, `@classmethod`, `@staticmethod`, and `@abstractmethod` are all decorators.

- `@classmethod` transforms a method so it receives the class (`cls`) instead of the instance (`self`).
- `@staticmethod` defines a method that does not receive either `self` or `cls`; it behaves like a regular function placed inside the class.
- `@abstractmethod` marks a method that must be implemented by subclasses when using an abstract base class.

Example:

```python
class Animal:
    @classmethod
    def hello(cls):
        print("Hello, I am an animal")

    @staticmethod
    def info():
        print("Animals are multicellular eukaryotic organisms")
```

General decorator syntax:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Suman")
```

- `@my_decorator` applies the decorator to `greet`.
- The original function is wrapped, allowing extra behavior before and after the call.

### Analogy
A decorator is like putting a protective case on your phone: the phone works the same, but the case adds new behavior (protection) without changing the phone itself.

### Why decorators matter in OOP
Decorators keep class methods organized and reusable. They let Python express special method behavior clearly, so method type and contract are visible at a glance.

### Example in the README examples
The `@classmethod` and `@staticmethod` examples shown above are the most common decorators in class-based OOP code.

---

## 11. Hands-on Project: EduPulse Management System

The `project/` subfolder contains a practical application of the OOP concepts described in this guide:

- **Classes & Inheritance**: `Persons` (Abstract Parent Class), `Student` (Child Class), and `Teacher` (Child Class).
- **Data Storage**: Persistent storage in `school_data.json`.
- **Interfaces**:
  - CLI application via [`main.py`](file:///c:/Users/87591/Desktop/OOPS/project/main.py)
  - Streamlit Light-Theme Web UI via [`app.py`](file:///c:/Users/87591/Desktop/OOPS/project/app.py)

For full details and instructions on running the app, see [project/README.md](file:///c:/Users/87591/Desktop/OOPS/project/README.md).

