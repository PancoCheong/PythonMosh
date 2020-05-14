### 05_class.py ###
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
