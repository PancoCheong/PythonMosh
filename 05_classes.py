### 05_class.py ###
'''
Python project hierarchical structure
    - Project → Package (folder) → Module (file) → Class → Function → Code

    
Problem: 
    - code repetition  
    - High maintenance cost later  
    - Low code readability  

Solution: functions  
    In a complete project, some features will be used repeatedly,  
    so we extract the code corresponding to these features.  
    When the functionality is needed, we just call it directly.  

Essence: encapsulation of some specific functionality  

Advantages:  
    a. Simplifies code structure and improves efficiency  
    b. Increases code reusability  
    c. Improves readability and maintainability  

Recommendation: whenever functionality is involved, try to implement it with functions
    
'''

# function - a reusable block of code that only runs when invoked
def my_fn(a, b, c=1, d=2):    # parameters c, d have default values
    print('I am a function')

my_fn(5, 10, d=99)  # Function must be called to execute, keep c with default values

# universal function that can accept any number of parameters
# Variable-Length Parameters:
# *args parameter collects any number of positional parameters into a tuple 
# **kwargs collects named parameters into a dictionary
def my_fn2(*args, **kwargs):
    print('args =',args)       # Tuple of positional parameters, output:args = (4, 5)
    print('kwargs =', kwargs)  # Dictionary of named parameters, output:kwargs = {'c': 77, 'd': 88}
    return args, kwargs

my_fn2(4, 5, c=77, d=88)       # 1st two: positional, last two: named
#
'''
Python strictly enforces Parameters Order 
    - For function definition:
        1. Positional parameters
        2. *args 
        3. Default parameters
        4. **kwargs
    - For function calls:
        1. Positional parameters first
        2. Named parameters second
'''
# function definition
def my_func(a, b, *args, d=7, e=8, **kwargs):
    # Implementation follows strict parameter ordering
    pass
    return a + b
# function call
result = my_func(2, 3, 4, 5, d=77, e=88, f=99, g=100)
#
# : int      Python 3.5 - type hints: input parameters is expected to be integer
# -> int     Python 3.5 - type hints: this function is expected to return a Boolean value
def add(a: int, b: int) -> int:
    return a + b
#
add(5, 10)
#
#
# Function nesting - function inside a function
def make_multiplier(factor):
    print(f'Creating a multiplier with factor {factor}')

    def multiplier(number):
        return number * factor  # inner function remembers "factor"

    return multiplier           # return the inner function, with preset factor value
#
# Create a function that always multiplies by 3
times_three = make_multiplier(3)       # return the inner function, output:Creating a multiplier with factor 3
print(times_three(10))                 # output:30

# Create a function that always multiplies by 5
times_five = make_multiplier(5)        # return the inner function, output:Creating a multiplier with factor 5
print(times_five(10))                  # output:50

#
#
# Function name: it is both 
#   1. call the function print_with_label() directly
#   2. alias_function - variable (object) pointing to that function
#      As long as a variable points to that function, it can be used to call the function
def print_with_label(x):
    print('print_with_label:', x)

print_with_label(1)               # print_with_label: 1
alias_function = print_with_label
alias_function(2)                 # print_with_label: 2


# Functions can be nested and call each other
def start_process():
    step_one()
    print('after called step_one   in start_process:', 1)

def step_one():
    step_two()
    print('after called step_two   in step_one:', 2)

def step_two():
    step_three()
    print('after called step_three in step_two:', 3)

def step_three():
    print('print in step_three:', 'three')

start_process()

''' output:
print in step_three: three
after called step_three in step_two: 3
after called step_two   in step_one: 2
after called step_one   in start_process: 1
'''



##### Anonymous function: lambda #####
#   Features:
#       A function without a name
#       Has an implicit return
#       Used to represent simple functions with return values
#
# normal function definition
def square(x):
    return x**2
#
print(square(5))         # 25
#
# => Anonymous function
f2 = lambda x: x**2
print(f2(5))             # 25

# with x, y parameters
f3 = lambda x, y: x + y
print(f3(3, 4))  # 7
#

# Higher-order functions 
# map: mapping to a function and apply it to each item of an iterable (list, tuple, etc)
n = map(lambda x: x**3, [1, 2, 3])
print(list(n))      # apply x**3 to each item, output: [1, 8, 27]

n = map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6])
print(list(n))      # apply x * y to each item from the two list 1*4, 2*5, 3*6, output: [4, 10, 18]

# filter: filtering, used to find data that meets certain conditions
n = filter(lambda x: x > 0, [1, -2, 3, -4, -5, 7, 6, -9])
print(list(n))      # apply the x > 0 condition to each item, return item if condition is True. output: [1, 3, 7, 6]


#
#
### Callback functions ###
#   Passing a function as a parameter into another function

def process_with_callback(factor, callback_func):  # callback_func=lambda x: x**2
    print('factor:', factor)              # factor: 3

    cb_func = callback_func(factor)       #   
    print('cb_func:', cb_func)            # cb_func: 9
#
# pass function as parameter
process_with_callback(3, lambda x: x**2)


#
def double(factor, callback_func):
    print('factor:', factor)             # factor: 3

    cb_func = callback_func(factor)      # callback, execute square_callback(3)
    print('cb_func:', cb_func)           # cb_func: 9
    return cb_func * 2                   # square_callback(3) * 2 

# callback_func is the callback function
def square_callback(x):
    return x**2

cb_result = double(3, square_callback)
print("cb_result:", cb_result)           # cb_result: 18
print()

# Custom filter
# filter: filtering, find data that meets certain conditions
# n = filter(lambda x: x > 0, [1, -2, 3, -4, -5, 7, 6, -9])

def custom_filter(callback_func, items):
    filtered = []
    for item in items:
        if callback_func(item):      # callback, check x > 0
            filtered.append(item)    # keep positive numbers
    return filtered

result = custom_filter(lambda x: x > 0, [1, -2, 3, -4, -5, 7, 6, -9])
print(result)  # [1, 3, 7, 6]


# sort(key=lambda)
profiles = [
    {'name': 'Zhang San', 'age': 18, 'score': 50, 'tel': 18866669999, 'sex': 'Unknown'},
    {'name': 'Li Si', 'age': 16, 'score': 88, 'tel': 18866668998, 'sex': 'Male'},
    {'name': 'Wang Wu', 'age': 17, 'score': 48, 'tel': 18866667995, 'sex': 'Female'},
    {'name': 'Chen Yijun', 'age': 61, 'score': 59, 'tel': 18866669998, 'sex': 'Unknown'},
    {'name': 'Chen Erjun', 'age': 49, 'score': 88, 'tel': 18866669396, 'sex': 'Male'},
    {'name': 'Chen Sanjun', 'age': 49, 'score': 61, 'tel': 18866668994, 'sex': 'Female'}
]

# Requirement 1: Sort profiles by age (ascending)
profiles.sort(key=lambda d: d['age'])               #dictionary 
print(profiles)

# Requirement 2: Sort profiles by score (descending)
profiles.sort(key=lambda d: d['score'], reverse=True)
print(profiles)


# Sort numbers in ascending order
persons = [
    ('Zhang San', 18),
    ('Li Si', 16),
    ('Wang Wu', 17),
    ('Chen Yijun', 61),
    ('Chen Erjun', 49),
    ('Chen Sanjun', 48)
]

persons.sort(key=lambda t: t[1])                    #tuple
print(persons)



### Function Exercise ###
# 1. Check whether a year is a leap year
#    Leap year conditions (OR):
#        1. Divisible by 4 but not divisible by 100
#        2. Divisible by 400
#    If either condition 1 or condition 2 is met → leap year

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2000))    # True,  can divide by 100, but it can also divide by 400
print(is_leap_year(2027))    # False
print(is_leap_year(2028))    # True  

# 2. Get the number of days in a given month
#    Note: In leap years and common years, February has a different number of days
def get_days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    return False  # could also raise ValueError for invalid month

# 3. Get the season of a given month
#    March–May: Spring
#    June–August: Summer
#    September–November: Autumn
#    December–February: Winter
def get_season(month: int) -> str:
    if month in [3, 4, 5]:
        return "Spring"
    if month in [6, 7, 8]:
        return "Summer"
    if month in [9, 10, 11]:
        return "Autumn"
    if month in [12, 1, 2]:
        return "Winter"

# 4. Check whether a number is prime
#    A prime number is a natural number greater than 1 
#    that has no factors other than 1 and itself.
def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(23))



### classes ###


from collections import namedtuple
from abc import ABC, abstractmethod
#
numbers = [1, 2]
numbers.append(3)
print(type(numbers))            # output:<class 'list'>
# create you own class
# shopping_cart.add()
# shopping_cart.remove()
# shopping_cart.get_total()
#
# point.draw()
# point.move()
# point.get_distance(1, 2)
#
# Class: blueprint for creating new objects.    eg. Human
# Object: instance of a class.                  eg. John, Mary, Jack
#
# convention: use Pascal case, no underscoe. eg. MyPoint
# all functions (aka. method) in a class should have at least ONE parameter
# by convention, it calls self
#
# when run command below, it generates a module (aka. package) name __main__
# python 05_class.py
#


class MyPoint:
    def draw(self):
        print("draw")


#
point = MyPoint()
point.draw()                        # output:draw
print(type(point))                  # output:<class '__main__.MyPoint'>
#                                   # __main__ is the name of the module
# check type (aka. class)
print(isinstance(point, MyPoint))   # output:True
print(isinstance(point, int))       # output:False
#
### constructor __init__ magic method, execute when you create object ###
# self - reference to current object
# when initialize a class, Python will internally create the object in memory,
# and set itself reference to that object
#
# Python will submit the 'self' parameter for you
#


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # by default, it prints is class type
    # override __str__() to print your values
    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    # by default, it compares memory address of two objects
    # override __eq__() to compare its values
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # override __gt__() to compare its values
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # override __add__() to calculate the value of two objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # define Class method, use @classmethod declorator
    # by convention, use cls as 1st parameter
    @classmethod
    def zero(cls):
        return cls(0, 0)            # call the constructor


#
point = Point(1, 2)
print(point.x)                      # output:1
point.draw()                        # output:Point (1, 2)
#
# Python allow to add attribute after object is created
point.z = 9
print(point.z)                      # output:9
#
# class attribute are shared across all instances of a class
Point.default_color = "yellow"
#
point2 = Point(3, 4)                # create one more object
point2.draw()                       # output:Point (3, 4)
# class
print(Point.default_color)          # output:yellow
# objects - note: point was created before change to yellow
print(point.default_color)          # output:yellow
print(point2.default_color)         # output:yellow
#
# change object attribute
point.default_color = "green"
print(point.default_color)          # output:green
print(point2.default_color)         # output:yellow
#
# Class vs Instance Method
# normal way to initial object
point = Point(0, 0)
# if the values are commonly use,
# you can create Class method to standardise it
point = Point.zero()
point.draw()                        # output:Point (0, 0)
#
## magic methods ##
# google search:python 3 magic methods
# https://rszalski.github.io/magicmethods/
#
# section: Representing your Classes
# print(point)                      # output:<__main__.Point object at 0x000001EEC04C4100>
#
# override point.__str__() magic method to print its values
print(point)                        # output:Point (0, 0)
#
### comparing object ###
point1 = Point(1, 2)
point2 = Point(1, 2)
#
# not equal because reference to different memory address
# print(point1 == point2)           # output:False
#
# equal because reference to same memory address
point3 = point2
# print(point3 == point2)           # output:True
#
# how to compare by value?
# section: Comparison magic methods
# override __eq__() magic method
#
print(point1 == point2)             # output:True
point3 = Point(3, 4)
print(point3 == point2)             # output:False
#
# how to implement: print(point3 > point2) by comparing values
# override __gt__()
print(point3 > point2)              # output:True
# __gt__ also work with less than, Python know how to handle it
print(point3 < point2)              # output:False
#
### arithmetic ###
# section: Normal arithmetic operator
# override __add__()
print(point3 + point2)              # output:Point (4, 6)
#
# Python common data structure: list, array, set
# they commonly known as container types
#
# make custom container type
# example: keep track of the number of various tags in a blog
# eg. how many articles do we have that are tagged with Python or JavaScript
#


class TagCloud:
    def __init__(self):
        # super().__init__()
        # self.tags = {}          # dict (public member)
        # __ - private member
        self.__tags = {}          # dict (private member)

    # override __str__() to print the values of __tags
    def __str__(self):
        return str(self.__tags)

    # override __getitem__(self, key) to get value
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # override __setitem__(self, key, value) to set value
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # override __len__(self) to get the item count
    def __len__(self):
        return len(self.__tags)

    # override __iter__() to return __tags dict
    def __iter__(self):
        return iter(self.__tags)

    # make the dict be case in-sensitive eg. lower()
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.tags)               # output:{'python': 3}
#
# override __getitem__()
# implement cloud["python"]
#
# override __setitem__()
# implement cloud["python"] = 10
#
# override __len__()
# implement len(cloud)
#
# override __iter__()           # cloud object will act like a dictionary object
# for tag in cloud:
#     print(tag)
#
print(cloud["python"])          # output:3
cloud["javascript"] = 10
print(cloud["javascript"])      # output:10
print(len(cloud))               # output:2
for tag in cloud:
    print(tag, end=" ")         # output: python javascript
print("")
#
### private member ###
#
### error - if access underlying class ###
# output: KeyError: 'PYTHON'
# because every key is in lower case, implement tag.lower() to solve it
# print(cloud.tags["PYTHON"])
#
# how to hide tags from outside - private members, prefix by __
# output: AttributeError: 'TagCloud' object has no attribute '__tags'
# it just show error to warning user when access it
# print(cloud.__tags["PYTHON"])
#
# output:{'_TagCloud__tags': {'python': 3, 'javascript': 10}}
# print(cloud)
#
### workaround to access it (hacking, not recommended to use it) ###
# get the prefix
# __dict__ - holds all the attributes in class
# output: {'_TagCloud__tags': {'python': 3, 'javascript': 10}}
# Python interpreter automatically reuses this attribute
# and prefixes it with the name of it's class
print(cloud.__dict__)
#
# workaround: still can access private member
print(cloud._TagCloud__tags)
#

# no longer works as private member now
# print(cloud.tags)               # output:{'python': 3}
#
# fix it
# override __str__()
print(cloud)                      # output:{'python': 3, 'javascript': 10}
#
#
### Property ###
#


class Product:
    def __init__(self, price):
        # self.price = price                    # replace by setter
        # self.set_price(price)                 # replace by @property
        self.price = price

    # def get_price(self):
    @property
    def price(self):                            # rename getter for @property
        return self.__price

    # def set_price(self, value):
    @price.setter
    def price(self, value):                     # rename setter for @price.setter
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # Pythonic way
    # price = property(get_price, set_price)    # replace by @property


# how to prevent input negative number, price should not be negative
# product = Product(-50)
#
# make it private member __price
# define getter and setter
# output: ValueError: Price cannot be negative.
# product = Product(-50)
#
# this is not a Pythonic - means not using Python's best practice
#
## use property ##
# an object in front of an attribute, allow us to get or set the value
# property(function_get, function_set, function_del, documentation)
# price = property(get_price, set_price)
#
product = Product(10)
# output:ValueError: Price cannot be negative.
# product.price = -1
#
# how to hide the get_price and set_price methods from outside world
# product.set_price(10)
# product.get_price()
#
# use @property decloration and rename getter and setter the function
# use price property directly
# @<property_name>.setter - for setter function
product.price = 99
print(product.price)            # output: 99
#
### comment out the setter function -> readonly property ###
# output: AttributeError: can't set attribute
# product.price = 100
#
### inheritance ###


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# class Mammal:

# Animal: Parent, Base class
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # call parent's __init__
        print("Mammal Constructor")
        self.weight = 2
    # def eat(self):
    #     print("eat")

    def walk(self):
        print("walk")

# apply the same to Fish class


class Fish(Animal):
    # eat method is in common for both Mammal and Fish
    # def eat(self):
    #     print("eat")

    def swim(self):
        print("swim")


#
# Concept: DRY - Don't repeat yourself
# either thru Inheritance or composition to avoid repeated code
#
# Inheritance - define the common behavior or common functions in a class
# then inherit them in other classes
#
# define class Animal
#
m = Mammal()
m.eat()                         # output:eat
m.walk()                        # output:walk
# add age attribute in Animal
print(m.age)                    # output:1
#
# check object type
print(isinstance(m, Mammal))    # output:True
# parent of Mammal - Animal class
# also True
print(isinstance(m, Animal))    # output:True
#
# Animal (or any class) inherits from object class (base of all class)
# even we don't define it, just like
# class Animal(object):
#
print(isinstance(m, object))    # output:True
#
# all classes have all o.* methods like __init__, __str__
# it inherits from object class
o = object()
#
# check sub-class
print(issubclass(Mammal, Animal))  # output:True
print(issubclass(Mammal, object))  # output:True
#
### method overriding ###
# copy __init__ constructor from Animal to Mammal
#
# no more: m.age
# output:AttributeError: 'Mammal' object has no attribute 'age'
# print(m.age)
# because Animal.__init__ is no longer executed
# it is replaced by Mammal.__init__
print(m.weight)                     # output:2
#
# call super().__init__() to execute Animal.__init__
# in this way, it extends the original method and adds weight attribute
print(m.age)                        # output:1
#
#
#
### Multi-level inheritance ###
# Employee -> Person -> LivingCreature -> Thing
# don't try to simulate the whole world
# only define what your software needs, either class or method
# eg. LivingCreature -> Thing may be not necessary
#
# ## Tips: limit the inheritance to ONE or TWO levels
#
# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")

# but... Chicken cannot fly, it should not have fly()


class Chicken(Bird):
    pass
#
#
### Multiple Inheritance ###
# (not recommended to use)
# good for inheritance if parent classes has no common methods
#
# it could lead to unexpected problem
# eg. which method to call if both have method under the same name
# if we change the order of inheritance, the result is different
# from      class Manager(Employee, Person):
# to        class Manager(Employee, Person):


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")

# change order of inheritance
# class Manager(Employee, Person):


class Manager(Person, Employee):
    pass


mgr = Manager()
# because Employee is at 1st position
# look up sequence: Manager --> Employee --> Person
# ---> class Manager(Employee, Person):
mgr.greet()             # output:Employee Greet
#
# change the order of inheritance
# ---> class Manager(Person, Employee):
mgr.greet()             # output:Person Greet
#
#
### good example for multiple inheritance ###


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swin(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
#
#
### Good example of inheritance ###
# one or two levels of inheritance
# don't have multiple inheritance
#
# eg. read a stream of data
#  1. from file
#  2. from network
#  3. from memory
# all these streams have a few things in common,
# like open them, close them, can read data from them
# but,
# how to read data is dependent upon the type of the stream
# reading data from file is different from reading data from network
#
#
### create customized exception type #


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # Python Abstract Base Class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # define common abstract method
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


#
#
### Abstract Base Class ###
# issue 1: Stream class is a abstract concept, no read() implementation
# we should use either FileStream or NetworkStream as it konws how to read data
# stream = Stream()
# stream.open()
#
# issue 2: no common interface
# FileStream and NetworkStream have read()
# however, if we implement MemoryStream, we can use dump() to read data
# which make it incompatibile to FileStream and NetworkStream
class MemoryStream(Stream):
    def dump(self):
        print("Reading data from memory")


#
# use abstract base class to solve
# it is a half-baked class
# 1. from abc import ABC, abstractmethod
# 2. class Stream(ABC):
# 3. define common interface methods ie. read() and write() etc
#    and @abstractmethod declorator to label them
#
# linter error:Abstract class 'Stream' with abstract methods instantiated
# stream = Stream()
#
# linter error:Abstract class 'MemoryStream' with abstract methods instantiated
# read() is not yet implemented, it is considered as abstract class that cannot be instantiated
# stream = MemoryStream()
#
#
### Polymorphism - the ability to take various forms ###
## define methods in the child class with the same name as defined in their parent class ##
## the handling logic doesn't necessary to know what type of object it is working with, and it calls the same method to perform the task ##
# from abc import ABC, abstractmethod
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


## pass in the different objects and performs the same task ##
# draw method
def draw(control):
    control.draw()


# drawAll method
def drawAll(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
txt = TextBox()
print(isinstance(ddl, UIControl))   # output:True
print(isinstance(txt, UIControl))   # output:True

draw(ddl)                           # output:DropDownList
draw(txt)                           # output:TextBox
#
#
# output:
# DropDownList
# TextBox
drawAll([ddl, txt])
#
# draw or drawAll methods do not know what kind of component it is working with.
# it simples call the draw() method of the passed-in object, regardless it is TextBox or DropDownList
# as all objects inherit from the abstract base class which defined
# @abstractmethod draw(), all its child object should have draw()
# This behavior is called Polymorphism
# Poly  - mean Many
# morph - mean Forms
# the draw() method is taking many different forms and this is determined at run time.
# we can be calling the draw() on TextBox, DropDownList or RadioButton...etc
#
### duck typing ###
#
# in below example:
# Polymorphism is still working without parent abstract class
# because controls - doesn't have specify object type
# as long as the object has the draw() method, it works
#
# Python terminology:
# if object walks like a duck, and quacks like a duck, it is a duck
# Python is dynamic type language, it doesn't check the type of objects.
# it only looks for the existence of certain methods in the objects.
#
# it is still a good practice to have abstract base class
# as it enforces a common interface or a common contract across all its derivatives.
# ie. they will have all methods defined by @abstractmethod
#
# class TextBox:
#     def draw(self):
#         print("TextBox")


# class DropDownList:
#     def draw(self):
#         print("DropDownList")

# # drawAll method - controls doesn't have specify object type
# def drawAll(controls):
#     for control in controls:
#         control.draw()
#
#
# Extending Built-in Types - inherit from str, list
# extending string class
class Text(str):
    def duplicate(self):
        return self + self


#
text = Text("Python")
# extend new method
print(text.duplicate())         # output:PythonPython
# use origin str method
print(text.lower())             # output:python
#
#


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("a")                # output:Append called
#
#
### data class ###
# class that only have data
#
# normal class as below


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Position(1, 2)
p2 = Position(1, 2)
# compare objects - without override __eq__(), it compares memory address
print(p1 == p2)                 # output:False
# print memory address
print(id(p1))                   # output:2612139892016
print(id(p2))                   # output:2612139892112
#
# override __eq__()
print(p1 == p2)                 # output:True
#
#
### use namedtuple to store data class ###
#
# no need to write __eq__ method
# cannot update value after the value is set,
# create new object to replace existing object for updating value
#
#from collections import namedtuple
# namedtuple(New Type Name, [Attribute_Name1, Attribute_Name2])

MyPosition = namedtuple("MyPosition", ["x", "y"])
p1 = MyPosition(x=1, y=2)
p2 = MyPosition(x=1, y=2)
# no need to override __eq__ to compare by values
print(p1 == p2)                 # output:True
print(p1, p2)                   # output:MyPosition(x=1, y=2) MyPosition(x=1, y=2)
#
# the object is immutable, cannot change value
# output:AttributeError: can't set attribute
# p1.x = 10
#
p1 = MyPosition(x=10, y=20)
print(p1)                       # output:MyPosition(x=10, y=20)





#### Revisit Python Data Classes ####

# C language: a procedural programming language (no classes)
# Java, C#, Objective-C, C++, Go, etc. are object-oriented (they have classes)

# In Python: everything is an object!

# Procedural Programming: a programming paradigm that focuses on the steps to solve a problem
# Object-Oriented Programming (OOP): a programming paradigm that focuses on the objects in the problem 
#   (emphasizes using classes to encapsulate the functions/behavior of these objects)


# Understanding Object-Oriented Programming
# Example: A dog eats food (sniff, lick, bite)
#   Analyze this using both procedural programming and object-oriented programming
#
# Procedural: first sniff, then lick, then bite (focus on process/steps)
# OOP: the dog is an object; it can sniff food, lick food, and bite food 
#   (focus on the object rather than the sequence of steps)


# 1. Procedural: first sniff, then lick, then bite (focus on process)
def smell():
    print('sniff')

def lick():
    print('lick')

def bite():
    print('bite')

smell()
lick()
bite()


# 2. Object-Oriented: the dog is an object; it can sniff food, lick food, and bite food 
#    (focus on the object, not the process)
# class is the keyword used to define a class
# PascalCase (capitalize the first letter of each word) is used for class names
#
class Dog:
    # Variable: attribute
    name = "Wangcai"

    # Functions: methods, behaviors
    def smell(self):
        print(self.name, 'sniffs')

    def lick(self):
        print(self.name, 'licks')

    def bite(self):
        print(self.name, 'bites')


# Create an object
dog = Dog()
dog.smell()
dog.lick()
dog.bite()


# Class and Object
#   A class is an abstraction of objects, a blueprint (class), a generalization of similar things.
#   An object is the concrete instance created from a class.
#
#   Class: the template of object, it does not occupy memory
#   Object: create a runtime based on class template, it occupies memory, and different objects occupy different memory

#   Class         Object
#   Person        Me, You, He 
#   Computer      Your Huawei computer, Her Mac Mini
#   Laptop        Your Huawei laptop, His MacBook
#   Boyfriend     Your specific boyfriend
#
# One class can create any number of objects.
# Example: A factory model for producing Huawei phones is a class.
#          Each actual phone produced is an object.


# Define a class
# All classes in Python by default inherit from `object`.
class Person(object):
    # Attributes: variables, static properties that describe features
    # Class attributes: usually accessed using the class name
    # name = "Jack"  # fixed value
    # age = 30

    # Method: initializer (constructor)
    #   1. Used to initialize attribute values
    #   2. Automatically called when creating an object
    def __init__(self, name, sex):
        # Object attributes: instance attributes, accessed via the object
        self.name2 = name
        self.sex2 = sex

    # Method: function belonging to the object, describes behavior
    def run(self):
        print(self.name2, "is running")


# Create objects
p = Person("Jay", 'Male')
print(p.name2, p.sex2)
p.run()

p2 = Person('Hannah', 'Female')
print(p2.name2, p2.sex2)
p2.run()


# Exercise
# 1. Create a Phone class
#      Attributes: color, size, price
#      Methods: call, play_game, chat

class Phone:
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def call(self):
        print('call')

    def play_game(self):
        print('play game')

    def chat(self):
        print('chat')

iphone16 = Phone('black', 6, 8000)
print(iphone16.color, iphone16.size, iphone16.price)


# 2. Example: Xiaomei walks Wangcai in Chaoyang Park [Note: Wangcai is a dog]
#   Class People:
#       Attribute: name
#       Method: walk_dog
#            def walk_dog(self, place, dog_name):
#                   "Xiaomei is walking Wangcai in Chaoyang Park"

class People:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog_name):
        print(f'{self.name} is walking {dog_name} in {place}')


xiaomei = People('Xiaomei')
xiaomei.walk_dog('Chaoyang Park', 'Wangcai')


# self:
#   1. Not a keyword, just a parameter name, but by convention we write `self`. 
#      (You don’t need to pass a value for self explicitly.)
#   2. `self` refers to the current object of the class 
#      (whichever object calls the method, `self` inside that method refers to that object).
#   3. Its purpose is to allow you to access other attributes or methods of the class from inside a method.


class Dog:
    def __init__(self, name):
        self.name = name
        print('__init__ method self:', id(self))
    
    def eat(self):
        print(self.name, 'likes to eat bones!')
        print('eat method self:', id(self))


# id(): memory address
#
# Create object
dog = Dog('Wangcai')            # __init__ method self: 2048163747248
# print(dog.name)           
dog.eat()                       # eat method self: 2048163747248
print('id(dog):', id(dog))      # id(dog): 2048163747248
print('*' * 100)

dog2 = Dog('Dahuang')           # __init__ method self: 2048163746720
dog2.eat()                      # eat method self: 2048163746720
print('id(dog2):', id(dog2))    # id(dog2): 2048163746720



# Constructor method: initialization method, automatically called when creating an object
#    __init__
# Destructor method: automatically called when an object is destroyed (for reference)
#    __del__

# Magic methods: methods with double underscores


class Animal:
    # Constructor
    def __init__(self, name):
        self.name = name
        print('Constructor: automatically called when the object is created!')

    # Destructor
    def __del__(self):
        # Here you could manually release resources, e.g., free memory or close files
        print('Destructor: automatically called when the object is destroyed!')


cat = Animal('Mimi')


import time
time.sleep(3)

del cat  # explicitly destroy the object

time.sleep(3)
print('end')




# Class attributes:
# Object attributes:

class Person:
    # Class attributes
    sex = 'Male'
    age = 30

    def __init__(self, name, age):
        # Object attributes
        self.name = name
        self.age = age


p = Person('Xiao Huang', 10)

# Accessing object attributes: can only be accessed through objects
print(p.name)
# print(Person.name)  # Error, cannot access object attributes via class name

# Accessing class attributes: recommended to use the class name
print(p.sex)
print(Person.sex)
print()


# Working with age
print(Person.age)  # 30, this is the class attribute
print(p.age)       # 10, object attribute takes priority

# Modifying age
Person.age = 40
print(Person.age)  # Class name can only modify class attribute age

p.age = 13  # Always modifies object attribute age, regardless of class attribute
print(p.age, Person.age)  # 13 40

# Summary:
#   Use objects to work with object attributes
#   Use class names to work with class attributes


# Extension:
#   Class attributes of the same class can be shared across objects 
#   created from that class (this applies to mutable types, e.g., lists)

class Dog:
    likes = ['bone']

    def __init__(self, name):
        self.name = name
        self.likes2 = ['bone']


dog1 = Dog('Xiaobai')
dog2 = Dog('Xiao Huang')

# Modify class attribute
Dog.likes.append('meat')
print(dog1.likes)  # ['bone', 'meat']
print(dog2.likes)  # ['bone', 'meat']

# Modify object attribute
dog1.likes2.append('chicken')
print(dog1.likes2)  # ['bone', 'chicken']
print(dog2.likes2)  # ['bone']



# Private attributes and private methods: add two underscores before the attribute or method name
# Public attributes and public methods


class Girl:
    def __init__(self, name, age):
        # Public attribute
        self.name = name
        # Private attribute:
        #   1. Can only be used inside the current class
        #   2. Attribute name must start with two underscores
        self.__age = age

    # Public method
    def dance(self):
        print(f'{self.name} is {self.__age} years old and can dance!')
        self.__sing()  # private method is accessible inside the class

    # Private method
    def __sing(self):
        print(f'{self.name} can sing')


# Object
g1 = Girl('Liu Yifei', 18)
print(g1.name)
#print(g1.__age)  # Private attribute, cannot be accessed outside the class
#                   AttributeError: 'Girl' object has no attribute '__age'
g1.dance()
#g1.__sing()      # Private method, cannot be accessed outside the class
#                   AttributeError: 'Girl' object has no attribute '__sing'

# Extension: Not recommended! Treat private attributes as private.
# Special case: can still be accessed internally using the name-mangled form: _ClassName__attribute
print(g1._Girl__age)
g1._Girl__sing()



# The purpose is to allow a function to be accessed like an attribute
#   1. Must have a return value
#   2. Cannot take parameters
# @property  # (important to know)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter: used to get the value
    @property
    def age(self):
        return self.__age

    # setter: used to modify the value
    @age.setter   
    def age(self, new_age):
        if new_age > 0:         # validate age before update
            self.__age = new_age


# Object
p = Person('Zhang San', 33)
print(p.age)   # 33 

p.age = 18     # would use the setter
print(p.age)   # 18

p.age = -1     # cannot set age to negative
print(p.age)   # 18



# Class:
#    Attributes: class attributes, object attributes, private attributes
#    Methods: object methods, private methods, class methods, static methods

class Person:
    age = 30  # class attribute

    def __init__(self, name):
        self.name = name  # object attribute

    # Object method, also called instance method
    def run(self):
        print('run')
        print(self.name)
        print(Person.age)
        self.__sleep()

    # Private method
    def __sleep(self):
        print('sleep')

    # Class method (important to know)
    # @classmethod
    #    1. Class methods can be called with the class name (recommended), or by an object
    #    2. Purpose: no need to create an object (saves object memory); methods can be used directly
    #    3. A class method has cls, not self, so it can access class attributes, other class methods, and static methods.
    @classmethod
    def eat(cls):  # cls represents the class
        print('eat')
        print(cls == Person)
        print(cls.age)

    # Static method (for reference)
    # @staticmethod
    #    1. Static methods can be called with the class name (recommended), or by an object
    #    2. Purpose: no need to create an object (saves object memory)
    #    3. No cls, no self. They cannot access any attributes or methods of the class..
    @staticmethod
    def game():
        print('game: static method')


# Object
# p = Person('Deng Chao')
# p.run()
Person.eat()
Person.game()



# Example (reference from standard library):
# import datetime
# dt = datetime.datetime(year=2030, month=1, day=2)
# print(dt.hour)
# datetime.datetime.fromtimestamp()




# Exercise
# Create a utility class Number, with:
# Class attribute:
#     num (initial value 10)
# Class methods:
#     add_num(cls)   → increase num by 1
#     sub_num(cls)   → decrease num by 1
#     mul_num(cls,n) → multiply num by n
#     div_num(cls,n) → divide num by n
# Static methods:
#     add(x, y): return the result of x + y
#     sub(x, y): return the result of x - y
#
# Without creating an object, call these methods and then print num.

class Number:
    num = 10

    @classmethod
    def add_num(cls):
        cls.num += 1

    @classmethod
    def sub_num(cls):
        cls.num -= 1

    @classmethod
    def mul_num(cls, n):
        cls.num *= n

    @classmethod
    def div_num(cls, n):
        cls.num /= n

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


Number.add_num()
Number.sub_num()
Number.mul_num(2)
Number.div_num(4)
print(Number.num)

print(Number.add(5, 4))  # 9
print(Number.sub(5, 4))  # 1



# Four major features of Object-Oriented Programming (OOP):
#   1. Encapsulation: Hide the details, expose only what’s necessary - Bundle attributes and methods inside a class, and control access to them. eg. use methods to update attributes
#   2. Inheritance: Avoid rewriting the same code; extend functionality - subclasses can inherit attributes and methods from parent classes
#   3. Polymorphism: One name, many forms - Different classes can define the same method name, but behave differently.
#   4. Abstraction: Focus on what an object does, not how it does it - Use abstract classes and interfaces to define common behavior.


# Inheritance: subclasses inherit attributes and methods from parent classes
#   Makes it easier to maintain and extend code

# Single inheritance: only one parent class

# Parent class (base class)
class IPad:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def movie(self):
        print('watching a movie')


# Subclass
class IPhone(IPad):
    def __init__(self, color, price, size):
        super().__init__(color, price)        # call the parent’s init method to initialize color and price
        # IPad.__init__(self, color, price)   # alternative: directly call the parent’s constructor
        self.size = size

    def call(self):
        print('can make phone calls')


phone16 = IPhone('red', 8000, 6)
print(phone16.color, phone16.price, phone16.size)
phone16.call()
phone16.movie()


# When to use inheritance:
#   1. A subclass extends functionality on top of what the parent provides
#   2. Extract common attributes and methods from different subclasses into a parent class
# Example:
#   Dog class: name, age, sleep, + dog-specific behavior
#   Cat class: name, age, sleep, + cat-specific behavior
#   We can extract the shared attributes and methods into an Animal class (as the parent),
#   and then Dog and Cat inherit from Animal.
#
# Single inheritance: Only 1 parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('loves sleeping')

# Subclass Dog
class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def eat(self):
        print('dogs love eating bones')

# Subclass Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def catch_mouse(self):
        print('cats can catch mice')


# Objects
dog = Dog('Wangcai', 3, 'male')
print(dog.name, dog.age, dog.sex)
dog.sleep()
dog.eat()

cat = Cat('Garfield', 10, 'yellow')
print(cat.name, cat.age, cat.color)
cat.sleep()
cat.catch_mouse()



# Multiple inheritance: Multiple parent classes (for understanding)
#
# 2 parent classes: Father, Mother
# 1 child class: Son
#
class Father:
    def __init__(self, name):
        self.name = name
    def smoke(self):
        print('Can smoke')

class Mother:
    def __init__(self, age):
        self.age = age
    def cook(self):
        print('Can cook')

# Child class
class Son(Father, Mother):
    def __init__(self, name, age, sex):
        # Father.__init__(self, name)  # Explicit call
        # Mother.__init__(self, age)
        
        # super(Son, self).__init__(name)
        super().__init__(name)         # Implicit call
        super(Father, self).__init__(age)

        self.sex = sex

    def play_game(self):
        print('Can play games')

son = Son('Xiaohong', 20, 'Male')
print(son.name, son.age, son.sex)
son.smoke()
son.cook()
son.play_game()

# Inheritance chain 
# Method Resolution Order MRO - a tuple that defines the order in which Python looks for methods and attributes when dealing with inheritance
# for multiple inheritance, Python needs a consistent strategy (ie. C3 linearization algorithm) to decide:
#     If I call a method, which parent class should Python check first?
print(Son.__mro__)
# (<class '__main__.Son'>,
#  <class '__main__.Father'>,
#  <class '__main__.Mother'>,
#  <class 'object'>
# )
#
# check sequence is : Son --> Father --> Mother --> object
#



### Polymorphism ###
# Overriding: method overriding, where a subclass defines a method 
# with the same name as a method in the parent class.

class Person:
    def run(self):
        print('run in Person (parent class)')

class Boy(Person):
    pass
    # Overriding: writing a method in the subclass with the same name as in the parent class
    #     The subclass method takes priority over the parent’s version.
    def run(self):
        print('run in Boy (subclass)')


boy = Boy()
boy.run()

p = Person()
p.run()




### Encapsulation ###
# Private attributes cannot be inherited:
#     Private attributes can only be used inside the class where they are defined.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def eat(self):
        print(self.name, 'eat')


class Boy(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def sleep(self):
        print('sleep')
        # print(self.__age)  # Cannot directly access parent’s private attribute in subclass
        self.eat()


boy = Boy('Xiao Ming', 20, 'Male')
print(boy.name)
# print(boy.__age)  # Cannot directly access a private attribute outside the class
boy.sleep()


### Abstraction ###
# import from Abstract Base Class
#     - The abc module in Python provides the tools to define abstract base classes (ABCs).
#         - An abstract class is a class that cannot be instantiated directly.
#         - It serves as a blueprint, forcing subclasses to implement certain methods.
#
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())    # 78.5 16


# By default, every Python object has a __dict__ that stores its attributes.
#     - can add new attributes
#     - require extra memory to store attributes
#
# __slots__ :  special class attribute, When you define __slots__, Python allocates space only for the attributes you list
#     - Restricts which attributes you can add to objects.
#     - Removes the per‑object __dict__ (unless you explicitly include it).
#     - Reduces memory usage, especially when creating many objects of the same class.
#     - Faster attribute access 

# Example 1: Without __slots__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
p.address = "123 Street"             # ✅ Works fine, dynamic attribute
print(p.__dict__)  
# {'name': 'Alice', 'age': 25, 'address': '123 Street'}


# Example 2: With __slots__
class Person:
    __slots__ = ["name", "age"]      # restrict attributes
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
# p.address = "123 Street"           # ❌ AttributeError: no attribute 'address'


# Example 3: Still allowing __dict__
class Person:
    __slots__ = ["name", "age", "__dict__"]  # allow custom attributes

p = Person("Alice", 25)
p.address = "123 Street"             # ✅ Works because __dict__ is included
print(p.__dict__)  
# {'address': '123 Street'}



class Person:
    # Restrict which attributes can be defined
    __slots__ = ['name', 'age', 'sex']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Xiao Ming', 10)
p.sex = "Male"                 # add an attribute to object p
print(p.name, p.age, p.sex)

# p2 = Person('Xiao Hei', 30)
# print(p2.name, p2.age)


# Special attributes: 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('running')


d = Dog('Wangcai', 3)

# print(d.__class__)
# print(Dog.__class__)
print(d.__dict__)  # dictionary {'name': 'Wangcai', 'age': 3}

# d2 = Dog(**{'name': 'Wangcai', 'age': 3})
# d2 = Dog(name='Wangcai', age=3)  # equivalent to above
# print(d2.__dict__)
# print(d.__module__)  # module name ‘__main__’

# Magic methods: usually called automatically
# __new__() : creates the object (called first)
# __init__() : initializes the object (called after __new__)
# __del__() : called when the object is deleted (called last)


# Operator overloading: advanced usage
class Number:
    def __init__(self, n):
        self.n = n

    # Operator overloading: addition
    def __add__(self, other):
        return self.n + other.n

    # __str__ : makes printing the object show the return value of __str__ (important to know)
    # def __str__(self):
    #     return f' -- {self.n} -- '

    def __repr__(self):
        return f' ** {self.n} ** '


n1 = Number(3)
n2 = Number(4)
print(n1 + n2)  # 7

print('*' * 100)
print(n1)
print([n1, n2])






