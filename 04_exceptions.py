import os
from timeit import timeit

### Exceptions ###
numbers = [1, 2]
# output:IndexError: list index out of range
# print(numbers[3])
#
# input:abc
# output:ValueError: invalid literal for int() with base 10: 'abc'
# age = int(input("Age: "))
#
#
# input:Age: aa
# output:
# Please enter integer for age!
# invalid literal for int() with base 10: 'aa'
# <class 'ValueError'>
# Execution continues
#
# input:Age: 11
# output:
# No exceptions were thrown
# Execution continues
try:
    age = int(input("input non-integer value to trigger ValueError exception  age: "))
except ValueError as ex:
    print("Please enter integer for age!")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")
#
#
### Handling different exception ###
# input:0
# output:ZeroDivisionError: division by zero
#
# note: only the first 'except' statement will be executed
# ie. 2nd ZeroDivisionError is not executed
# input:0
# output:You didn't enter a valid age.
try:
    age = int(input("Input 0 to trigger ZeroDivisionError for age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("No exceptions were thrown")
#
### clean up - finally: ###
# output:FileNotFoundError: [Errno 2] No such file or directory: 'non_exist_file.txt'
# NameError: name 'my_file' is not defined
#
# r for reading (default)
# w for writing, create file if not exist; if exists, it truncates the file
# x for creating the specified file, returns an error if the file exists
# a+ opens for appending
#
# r+ opens for reading and writing (cannot truncate a file)
# w+ for writing and reading (can truncate a file)
# rw+ (removed in Python 3)
#       Note: indeed r+, rw+ and w+ has no different in Linux
#
# rb+ reading or writing a binary file
# wb+ writing a binary file
#
# read more: https://stackabuse.com/file-handling-in-python/
# open(filename, mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#
# f = open("myfile.txt", "r+")
# text = f.read()
# f.truncate(0)
# f.seek(0, 0)
# print(f.read())
# f.close()

#import os
### remove file ###
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

## remove folder ###
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")
#
#
file = open("app.py", 'r')
try:
    # way 1: read whole file into single string, include \n
    text = file.read()
    print(type(text))       # output:<class 'str'>
    print(text)

    # way 2: read line by line, slower, but use less memory
    while True:
        text_line = file.readline()
        if text_line:
            print(type(text_line), text_line)
        else:
            break

    # way 3: read whole file, use list to store each line
    text_lines = file.readlines()
    print(type(text_lines), text_lines)
    for line in text_lines:
        print(type(line), line)
except (FileNotFoundError):
    print("file is not found.1")
else:
    print("No exceptions were thrown")
finally:
    file.close()

### with statement - auto-close file when exist the code block###
# finally: is not required
try:
    with open("app.py", 'r') as file:
        # open two files
        # with open("app.py", 'r') as file, open("another.txt") as target:
        print("%s file is opened." % file.name)
        text = file.read()
        print(text)
## magic method __myMethod__ ##
# any object has enter and exit magic methods
# it supports context management protocol,
        # file.__enter__
        # file.__exit__
# we can use with statement,
# Python will auto call exit method to release external resource

except (FileNotFoundError):
    print("file is not found.")
else:
    print("No exceptions were thrown")
#
#
# Google search: python 3 built in exceptions
# https://docs.python.org/3/library/exceptions.html
# scroll to bottom: Exception hierarchy


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


# output:Age cannot be 0 or less
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


### cost of raising exception ###
# time the execution duration
#from timeit import timeit

# change print statement by pass statement
# to avoid print message 10000 times
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
#
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
#
# don't raise exception if you can handle it in other way
# as it degrades the performance
#
# output:
# first code  = 0.007155099999999859
# second code = 0.0036609000000003
print("first code  =", timeit(code1, number=10000))
print("second code =", timeit(code2, number=10000))
