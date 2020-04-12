# 03_data_structure
from array import array
from collections import deque
import random
import string

# list - sequence of objects that can be a list,
# can be multiple types in a single list
letters = ['a', 'b', 'c']
print(letters)          # output:['a', 'b', 'c']
# matrix 2-dimension list
matrix = [[1, 2], [3, 4]]
print(matrix)           # output:[[1, 2], [3, 4]]
print(matrix[1])        # output:[3, 4]
print(matrix[1][1])     # output:4
# create list with same initial values
checklist = [False] * 5
# output:[False, False, False, False, False]
print(checklist)
# combine 2 list
combined = checklist + letters
# output:[False, False, False, False, False, 'a', 'b', 'c']
print(combined)
# convert to list
range_to_list = list(range(2, 6))
print(range_to_list)        # output:[2, 3, 4, 5]
string_to_list = list("Panco")
print(string_to_list)       # output:['P', 'a', 'n', 'c', 'o']
# count of list
print(len(string_to_list))  # output:5

### assign item ###
print(string_to_list[0])    # output:P
print(string_to_list[-1])   # output:o
print(string_to_list[1:3])  # output:['a', 'n']
print(string_to_list[3:])   # output:['c', 'o']
print(string_to_list[:3])   # output:['P', 'a', 'n']
# step of 2
print(string_to_list[::2])  # output:['P', 'n', 'o']
numbers = list(range(10))
# even numbers, odd numbers
print(numbers[::2])  # even,  output:[0, 2, 4, 6, 8]
print(numbers[1::2])  # odd,  output:[1, 3, 5, 7, 9]
# in reverse order
print(numbers[::-1])  # reverse, output:[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# update item
string_to_list[-2] = 'K'
print(string_to_list[3:])   # output:['K', 'o']
#
### unpacking list ###
# traditional way
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
# in Python, number of variables must = numbers of items in list
first, second, third = numbers
print(second)               # output:2
# pack the remaining items to separate list
numbers = list(range(1, 9))
first, second, *others = numbers
print(type(others))         # output:<class 'list'>
print(others)               # output:[3, 4, 5, 6, 7, 8]
first, *others, last = numbers
print(last)                 # output:8

### loop over list ###
# easy way to generate list of letters
# output:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',.....,'z']
# way 1
#import string
letters1 = list(string.ascii_lowercase)
# way 2 - ASCII code (A-Z:65-90, a-z:97-122)
letters2 = list(map(chr, range(97, 123)))
letters3 = list(map(chr, range(ord('a'), ord('z')+1)))
print(letters1)
print(letters2)
print(letters3)
# loop
# print the content
letters = list(map(chr, range(ord('a'), ord('g')+1)))
for letter in letters:
    print(letter, end=" ")      # output:a b c d e f g
print("")
# print the content with index position - enumerate()
# letter is tuple, like a readonly list, cannot add item
for letter in enumerate(letters):
    # output:(0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e') (5, 'f') (6, 'g')
    print(letter, end=" ")
print("")
# access the index and value
for letter in enumerate(letters):
    # output:0 a , 1 b , 2 c , 3 d , 4 e , 5 f , 6 g ,s
    print(letter[0], letter[1], ',', end=" ")
print("")
# better way to get index and value - use unpack
# item = (0, 'a')
# index, letter = item
for index, letter in enumerate(letters):
    # output:0 a , 1 b , 2 c , 3 d , 4 e , 5 f , 6 g ,s
    print(index, letter, ',', end=" ")
print("")

# add or remove item
letters.append("A")
print(letters)      # output:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'A']
# insert
letters.insert(3, "b")
print(letters)      # output:['a', 'b', 'c', 'b', 'd', 'e', 'f', 'g', 'A']
# remove at the end of the list
letters.pop()
print(letters)      # output:['a', 'b', 'c', 'b', 'd', 'e', 'f', 'g']
# remove at index
letters.pop(5)
print(letters)      # output:['a', 'b', 'c', 'b', 'd', 'f', 'g']
# remove by value (1st match)
letters.remove('b')
print(letters)      # output:['a', 'c', 'b', 'd', 'f', 'g']
# to remove all, use loop
letters[1] = 'g'
letters[3] = 'g'
print(letters)      # output:['a', 'g', 'b', 'g', 'f', 'g']
# keep every element that doesn't equal value
# letters = (letter for letter in letters if letter != 'g') # this create a new list
# letters[:] - this can mutate the existing list
letters[:] = (letter for letter in letters if letter != 'g')
print(letters)      # output:['a', 'b', 'f']
# other way to remove item - del function
del letters[0:2]
print(letters)      # output:['f']
# remove all
letters.clear()
print(letters)      # output:[]


### finding item ###
letters = list(map(chr, range(ord('a'), ord('c')+1))) * 2
print(letters)                  # output:['a', 'b', 'c', 'a', 'b', 'c']
print(letters.index('b'))       # output:1
if 'Z' in letters:              # check if 'Z' is existed in list
    # otherwise, it prompts ValueError: 'Z' is not in list
    print(letters.index('Z'))
# count number of item in list
print(letters.count('b'))       # output:2
print(letters.count('Z'))       # output:0


### sort list ###
#import random
# generate 10 random number with value between 0 to 99
random_numbers = random.sample(range(100), 10)
# generate 10 random number with value between -10 to 10
random_numbers = [random.randrange(-10, 10) for _ in range(10)]

# output:[44, 77, 36, 15, 51, 84, 18, 19, 62, 41]
print(random_numbers)
numbers = [44, 77, 36, 15, 51, 84, 18, 19, 62, 41]
# sort in ascending order
numbers.sort()
print(numbers)          # output:[15, 18, 19, 36, 41, 44, 51, 62, 77, 84]
# sort in descending order
numbers.sort(reverse=True)
print(numbers)          # output:[84, 77, 62, 51, 44, 41, 36, 19, 18, 15]
# built-in sort function - create a new list, original unchanged
print(sorted(numbers))  # output:[15, 18, 19, 36, 41, 44, 51, 62, 77, 84]
# output:[84, 77, 62, 51, 44, 41, 36, 19, 18, 15]
print(sorted(numbers, reverse=True))

### sort tuple in list ###
products = [
    ("Item A", 10.0),
    ("Item C", 9.0),
    ("Item B", 14.0)
]
# output:[('Item A', 10.0), ('Item C', 9.0), ('Item B', 14.0)]
print(products)
products.sort()
# output:[('Item A', 10.0), ('Item B', 14.0), ('Item C', 9.0)]
print(products)
# define a sort function
# pass-in the function name


def sort_product(product):
    return product[1]   # sort by price


# TypeError: sort() takes no positional arguments
# products.sort(sort_product)
# solution: key=
# sort by price ascending
products.sort(key=sort_product)
print(products)  # output:[('Item C', 9.0), ('Item A', 10.0), ('Item B', 14.0)]
# sort by price descending
products.sort(key=sort_product, reverse=True)
print(products)  # output:[('Item B', 14.0), ('Item A', 10.0), ('Item C', 9.0)]


### use lambda to implement sort function ###
# lambda parameter:return_expression
products.sort(key=lambda product: product[1])
print(products)  # output:[('Item C', 9.0), ('Item A', 10.0), ('Item B', 14.0)]


### map function ###
# extract price from products
# traditional way
prices = []
for product in products:
    prices.append(product[1])
print(prices)               # output:[9.0, 10.0, 14.0]

# in Python, use map
x = map(lambda product: product[1], products)
print(x)                    # output:<map object at 0x00000187845127C0>
for price in x:
    print(price, end=" ")   # output:9.0 10.0 14.0
print("")
# direct convert map object to list
prices = list(map(lambda product: product[1], products))
print(prices)               # output:[9.0, 10.0, 14.0]

### filter function ###
# get the list of product which price is >= 10.0
filtered = list(filter(lambda product: product[1] >= 10, products))
print(filtered)             # output:[('Item A', 10.0), ('Item B', 14.0)]


### list comprehensions ###
# preferred way to use (rather than map or filter)
# it is cleaner in syntax and faster to process
# syntax: [expression for item in items]
# prices = list(map(lambda product: product[1], products))
# same as above map function
prices = [product[1] for product in products]
print(prices)               # output:[9.0, 10.0, 14.0]
# filtered = list(filter(lambda product: product[1] >= 10, products))
# same as above filter function
filtered = [product for product in products if product[1] >= 10]
print(filtered)             # output:[('Item A', 10.0), ('Item B', 14.0)]


### zip function ###
list1 = ['A', 'B', 'C']
list2 = ['11', 12, 13]
# combine list of tuple
# list() to convert <zip object at 0x0000017FD4C36480>
print(list(zip(list1, list2)))  # output:[('A', '11'), ('B', 12), ('C', 13)]
# output:[('x', 'A', '11'), ('y', 'B', 12), ('z', 'C', 13)]
print(list(zip("xyz", list1, list2)))

### stacks ###
# stack of items, eg. stack of book on table
# Last In, First Out (FIFO)
# simulate the browser session
browsing_session = []
browsing_session.append('url_1')
browsing_session.append('url_2')
browsing_session.append('url_3')
print(browsing_session)             # output:['url_1', 'url_2', 'url_3']
last = browsing_session.pop()
print(last)                         # output:url_3
print(browsing_session)             # output:['url_1', 'url_2']
# Falsy value - empty []
# disable "go back" button in browser if browsing session is empty
if not browsing_session:  # if empty
    print("disable")
else:
    print("redirect", browsing_session[-1])  # output:redirect url_2


### Queue ###
# Queue in the real world
# Frist in, Frist Out (FIFO)
# [1, 2, 3, 4] ==> [2, 3, 4] # all item shift 1 position forward
# more efficient to use dequeue
#from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)        # output:deque([2, 3])
if not queue:
    print("empty queue")


### tuple ###
# contain a sequence of objects
# read-only list - use to prevent accidental modification
# it is immutable
# cannot modify the sequence, modify existing item
# cannot add or remove object
point1 = (1, 2)  # parenthesis can be omitted
point2 = 1, 2
point3 = 1,
point4 = ()
print(type(point1))     # output:<class 'tuple'>
print(type(point2))     # output:<class 'tuple'>
print(type(point3))     # output:<class 'tuple'>
print(type(point4))     # output:<class 'tuple'>
print(point1)           # output:(1, 2)
print(point2)           # output:(1, 2)
print(point3)           # output:(1,)
print(point4)           # output:()
## concat tuple ##
point = (1, 2) + (3, 4)
print(point)            # output:(1, 2, 3, 4)
# repeat the content
point = (1, 2) * 3
print(point)            # output:(1, 2, 1, 2, 1, 2)
# convert list to tuple
point = tuple([1, 2])
print(point)            # output:(1, 2)
point = tuple("Panco")
print(point)            # output:('P', 'a', 'n', 'c', 'o')
## access tuple ##
point = (1, 2, 3)
print(point[0])         # output:1
print(point[0:2])       # output:(1, 2)
# unpack the tuple
x, y, z = point
print(y)                # output:2
# check exist
if 3 in point:
    print("3 exists")   # output:3 exists

# immutable object
# output:TypeError: 'tuple' object does not support item assignment
# point[0] = 10


### swapping variable ###
x = 10
y = 11

# traditional way: swap need third variable
temp = x
x = y
y = temp
print(f"x={x}, y={y}")  # output:x=11, y=10

# in Python
x = 10
y = 11
x, y = y, x             # same as x, y = (y, x) # unpack
print(f"x={x}, y={y}")  # output:x=11, y=10

# use the unpack syntax, that's why we can initialize multiple variable
a, b, c = 1, 2, 3       # tuple () is omitted
print(c)                # output:3


# Array ##
# store only single data type
# use less memory than list
# process data faster
# better for large data set (eg. 10,000 or more records)
# module name array, class name array as well
#from array import array
# google search: python 3 typecode
# https://docs.python.org/3/library/array.html
# 'i'		signed int		int					2 bytes
# 'f'		float			float				4 bytes
# 'u'		Py_UNICODE		Unicode character	2 bytes
# array(typecode, list)
numbers = array('i')    # create empty int array
numbers = array('i', [1, 2, 3, 1, 2, 3])
numbers.append(2)
numbers.insert(1, 4)
print(numbers)          # output:array('i', [1, 4, 2, 3, 1, 2, 3, 2])
numbers.pop()           # remove last value 2
numbers.remove(3)       # remove 1st value 3
print(numbers)          # output:array('i', [1, 4, 2, 1, 2, 3])
print(numbers[0:3])     # output:array('i', [1, 4, 2])
print(numbers.count(2))  # output:2
print(numbers.typecode)  # output:i
print(numbers.index(4))  # output:1
numbers.extend(range(10, 13))  # add items from iterable
# output:array('i', [1, 4, 2, 1, 2, 3, 10, 11, 12])
print(numbers)
new_num = [20, 21]
numbers.fromlist(new_num)
# output:array('i', [1, 4, 2, 1, 2, 3, 10, 11, 12, 20, 21])
print(numbers)
numbers.reverse()
# output:array('i', [21, 20, 12, 11, 10, 3, 2, 1, 2, 4, 1])
print(numbers)
num_list = numbers.tolist()
# output:[21, 20, 12, 11, 10, 3, 2, 1, 2, 4, 1]
print(num_list)
#
# Error:
# single data type only
# output:TypeError: integer argument expected, got float
# numbers[2] = 9.99
# output:ValueError: array.remove(x): x not in array
# numbers.remove(0)      # remove non-existed value
#
#
# usage:
# append() -- append a new item to the end of the array
# buffer_info() -- return information giving the current memory info
# byteswap() -- byteswap all the items of the array
# count() -- return number of occurrences of an object
# extend() -- extend array by appending multiple elements from an iterable
# fromfile() -- read items from a file object
# fromlist() -- append items from the list
# frombytes() -- append items from the string
# index() -- return index of first occurrence of an object
# insert() -- insert a new item into the array at a provided position
# pop() -- remove and return item (default last)
# remove() -- remove first occurrence of an object
# reverse() -- reverse the order of the items in the array
# tofile() -- write all items to a file object
# tolist() -- return the array converted to an ordinary list
# tobytes() -- return the array converted to a string
#
#

### Set ###
# collection with no duplicate - unique values in set
# cannot access set by index, it stores data un-orderly.
numbers = [1, 1, 2, 3, 4, 2, 4]
first = set(numbers)
print(first)          # output:{1, 2, 3, 4}
print(type(first))    # output:<class 'set'>
second = {1, 4}
second.add(5)
second.remove(4)
print(second)           # output:{1, 5}
print(len(second))      # output:2
# union of two sets - return new set
print(first | second)   # output:{1, 2, 3, 4, 5}
# intersection of two sets - return new set
print(first & second)   # output:{1}
# difference of two sets - return new set
# item in first, which doesn't exist in second
print(first - second)   # output:{2, 3, 4}
# item in second, which doesn't exist in first
print(second - first)   # output:{5}
# semantic difference of two sets - return new set
# item either in first or second, but not both
print(first ^ second)   # output:{2, 3, 4, 5}
if 1 in first:
    print("1 exists")   # output:1 exists
#
# Error:
# data in set is not stored in sequence
# output:TypeError: 'set' object is not subscriptable
# print(first[0])
