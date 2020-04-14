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
        self.tags = {}          # dict

    # override __getitem__(self, key)
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # override __setitem__(self, key, value)
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # override __len__(self)
    def __len__(self):
        return len(self.tags)

    # override __iter__()
    def __iter__(self):
        return iter(self.tags)

    # make the dict be case insensitive
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)               # output: {'python': 3}
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

