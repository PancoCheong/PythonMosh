### Class ###
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
# all function in a class should have at least ONE parameter
# by convention, it calls self
#


class MyPoint:
    def draw(self):
        print("draw")


#
point = MyPoint()
point.draw()                        # output:draw
print(type(point))                  # output:<class '__main__.Point'>
#                                   # __main__ is the name of the module
# check type
print(isinstance(point, MyPoint))   # output:True
print(isinstance(point, int))       # output:False
#
### constructor __init__ magic method, execute when you create object ###
# self - reference to current object
# when initialize a class, Python will internally create the object in memory,
# and set itself reference to that object
#
# Python will submit the self parameter for you
#


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # override __str__()
    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    # override __eq__()
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # override __gt__()
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # override __add__()
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # define Class method, use @classmethod declorator
    # by convention, use cls as 1st parameter
    @classmethod
    def zero(cls):
        return cls(0, 0)       # call the constructor


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
print(Point.default_color)          # output:yellow
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
# section: Representing your Classes
# print(point)      # output:<__main__.Point object at 0x000001EEC04C4100>
# override point.__str__() magic method
print(point)        # output:Point (0, 0)
#
### comparing object ###
point1 = Point(1, 2)
point2 = Point(1, 2)
# no equal because reference to different memory address
# print(point1 == point2)       # output:False
# equal because reference to same memory address
# point3 = point2
# print(point3 == point2)       # output:True
#
# how to compare by value?
# section: Comparison magic methods
# override __eq__() magic method
#
print(point1 == point2)         # output:True
point3 = Point(3, 4)
print(point3 == point2)         # output:False
#
# how to implement: print(point3 > point2)
# override __gt__()
print(point3 > point2)          # output:True
# __gt__ also work with less than, Python know how to handle it
print(point3 < point2)          # output:False
#
### arithmetic ###
# section: Normal arithmetic operator
# override __add__()
print(point3 + point2)          # output:Point (4, 6)
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
        # self.tags = {}          # dict
        # __ - private member
        self.__tags = {}          # dict

    # override __str__()
    def __str__(self):
        return str(self.__tags)

    # override __getitem__(self, key)
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # override __setitem__(self, key, value)
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # override __len__(self)
    def __len__(self):
        return len(self.__tags)

    # override __iter__()
    def __iter__(self):
        return iter(self.__tags)

    # make the dict be case insensitive
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
# override __iter__()
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
# because every key is in lower case
# print(cloud.tags["PYTHON"])
#
# how to hide tags from outside - private members
# output: AttributeError: 'TagCloud' object has no attribute '__tags'
# it just show error to warning user when access it
# print(cloud.__tags["PYTHON"])
#
# output:{'_TagCloud__tags': {'python': 3, 'javascript': 10}}
# print(cloud)
#
### workaround to access it ###
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

# no longer works
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
# comment out the setter function -> readonly property
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
print(isinstance(m, Mammal))    # output:True
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
mgr.greet()             # output:Employee Greet
#
# change the order of inheritance
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
