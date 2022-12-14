import string

#output:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters1 = list(string.ascii_lowercase)  

# way 2 - ASCII code (A-Z:65-90, a-z:97-122)
letters2 = list(map(chr, range(97, 123)))
letters3 = list(map(chr, range(ord('a'), ord('z')+1)))
print(letters1)
print(letters2)
print(letters3)


print(1, 2, 3)

numbers = [1, 2, 3]
print(numbers)    
print(*numbers)                                 # output:1, 2, 3



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
point.draw(point)                   # output:Point (1, 2)  # you can pass in the point object;however, people always omitted




#sales1.py
#module name by convention: all lower cases and _

def calc_tax():
    print("calc_tax")

def calc_shipping():
    print("calc_shipping")
