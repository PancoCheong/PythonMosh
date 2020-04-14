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

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


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
