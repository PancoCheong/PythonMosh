import os
from timeit import timeit

### Exceptions ###

# Exception handling

# Error: happens before the code runs (compile-time issues), must be fixed first
# Exception: code runs but raises an error at runtime


# Exception handling: used when there is some probability of an exception occurring
# try-except:
#   Try to execute the code in try, if an error occurs go to except, otherwise skip except
#   Purpose: prevent the program from terminating due to errors, exceptions can be caught by except

# a = 0
# n = 3 / a
# print('An error occurred above, the program stopped, this will not be executed')

try:
    a = 2
    n = 3 / a
    print(n)
except:
    print('An error occurred')

print('Even though an error happened above, I can still execute this part')


# This way is recommended (important to know)
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:
    print(e)           # division by zero
    print(type(e))     # <class 'ZeroDivisionError'>
    print('Error occurred')

try:
    a = 2
    n = 3 / a
    print(n)         # 1.5
    l = []
    print(l[0])
except ZeroDivisionError as e:
    print(e)         # division by zero
    print(type(e))   # <class 'ZeroDivisionError'>
    print('Error occurred')
except IndexError as e:
    print(e)                              # list index out of range
    print('Error occurred: IndexError')   # Error occurred: IndexError


print()
# try-except-else  (for reference)
#   Try to execute code in try; if an error occurs go to except, otherwise go to else
try:
    a = 3
    n = 3 / a
    print(n)
except Exception as e:
    print("error:", e)
else:
    print('No problem')


# try-except-finally (for reference)
#   Try to execute code in try; if an error occurs go to except; finally always runs
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:
    print("error:", e)
finally:
    print('No matter what, I will always run this at the end')


# Python built-in exception types:
# Exception	              Triggered When...	               Example
# AttributeError	      Missing attribute/method	       "hi".uppercase
# NameError	              Variable not defined	           print(age)
# IndexError	          Index out of list/tuple range	   [1,2,3][5]
# ZeroDivisionError	      Dividing by zero	               100/0
# KeyError	              Missing dictionary key	       {"a":1}["b"]
# FileExistsError	      Making a file/dir that exists	   os.mkdir("x") again
# FileNotFoundError	      File doesn’t exist	           open("no.txt")
# ImportError	          Import fails	                   import fake
# IndentationError	      Wrong indentation	               Misaligned code
# SyntaxError	          Code invalid syntax	           if True print()
#
#### Raise an exception manually ####
# raise NameError("sorry! my mistake")
# raise IndexError("wrong index")

# Assertion assert #
def divide_by(n):
    # check "n is not zero"
    assert n != 0, "❌ Error: cannot divide by zero!"
    print(10 / n)
#
divide_by(2)  # ✅ Prints 5.0
divide_by(0)  # ❌ AssertionError: Error: cannot divide by zero!






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

# File operations:
#  1. Open file
#  2. Work with file (read / write)
#  3. Close file
#
# 1. Open file
# open(file, mode='r')
#   file: path of the file to open
#   mode:
#       r   : read-only, error if file does not exist (default)
#       w   : write (overwrite/clear), create file if not exist; if exists, it truncates the file
#       x   : creating the specified file, returns an error if the file exists
#       a   : append write, creates the file if it does not exist
#       a+  : opens for appending
#
#       r+  : opens for reading and writing (cannot truncate a file)
#       w+  : writing and reading (can truncate a file)
#       rw+ :(removed in Python 3)
#             Note: indeed r+, rw+ and w+ has no different in Linux
#
#       rb  : read-only binary, error if file does not exist
#       wb  : write binary (overwrite/clear), creates the file if it does not exist      
#       rb+ : reading or writing a binary file
#       wb+ : writing a binary file
#       ab  : append write binary, creates the file if it does not exist
#
# Mode	File must exist?	Truncate file?	Write position	                      Can read?	   Can write?
#  r	  ✅ Yes	              ❌ No	     Overwrites nothing, read-only	           ✅	      ❌
#  r+	  ✅ Yes	              ❌ No	     Beginning (overwrite as you write)	       ✅	      ✅
#  w	  ❌ No	              ✅ Yes	     Beginning (overwrite as you write)        ❌	      ✅
#  w+	  ❌ No	              ✅ Yes	     Beginning	                               ✅	      ✅
#  a	  ❌ No	              ❌ No	     End	                                   ❌	      ✅
#  a+	  ❌ No	              ❌ No	     End (writing always appends)	           ✅  	      ✅
#
#
# read more: https://stackabuse.com/file-handling-in-python/
#       open(filename, mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#
# fp = open('image.jpg', 'rb')                      # reading as binary
#
# f = open("myfile.txt", "r+", encoding='utf-8')    # use encoding for non-binary files
# text = f.read()       # read all content
# f.readline()          # read one line at a time, will continue line by line
# f.readlines()         # read all lines into a list  ['hello\n', 'abcdef']
# f.read(3)             # read 3 characters
# f.truncate(0)         # truncate file to 0 bytes
# f.seek(0, 0)          # move cursor to the beginning
# f.close()             # close file
#
# f.write('hello Mark'.encode())  # write string, need to encode for binary file
# 
#
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


# Pathlib - recommended library to work with files
# object-oriented, easier for path manipulation.
from pathlib import Path
current_folder = Path.cwd()  #returns as a Path object (can join paths, check existence, etc.).
print(current_folder)


import os
# os is used to access system functions, mainly for working with files or folders
print(os.name)      # nt means Windows operating system
print(os.getcwd())  # current directory


# Create a directory: mkdir()  → raises an error if the folder already exists
# Create nested directories: makedirs('a/b/c')
if not os.path.exists('hello'):
    os.mkdir('hello')

# os.makedirs('a/b/c')


# Delete an empty directory: rmdir  (for reference)
# os.rmdir('hello')

# Delete a file: remove  (for reference)
# os.remove('aa.txt')

# Rename: rename (for reference)
# os.rename('hello', 'hello2')



# listdir(): returns a list of all files or folder names in the specified directory
dir_list = os.listdir(r'C:\MyCode')
print(dir_list)


# os.path
#  os.path.exists : check if a file or folder exists
#  os.path.isfile() : check if it is a file
#  os.path.isdir() : check if it is a directory
print(os.path.exists(r'C:\MyCode\Python'))  # True
print(os.path.isfile(r'C:\MyCode\Python'))  # False
print(os.path.isdir(r'C:\MyCode\Python'))  # True


# Join paths
print(os.path.join(r'C:\MyCode\Python', 'a.py'))
# C:\MyCode\Python\a.py


# Requirement: print the absolute path of all subdirectories/files under a given directory
path = r'C:\MyCode\Python'
dir_list = os.listdir(path)
# print(dir_list)
for dir in dir_list:
    # Concatenate paths
    path2 = os.path.join(path, dir)
    # print(path2)

    if os.path.isfile(path2):
        print("File:", path2)
    else:
        print('Directory:', path2)


# Absolute path: starts from the drive letter
# Relative path: starts from the directory of the current file

# os.path.split : split path into directory and filename (for reference)
# print(os.path.split(r'C:\Users\01_os.py'))
# ('C:\\Users', '01_os.py')

# os.path.splitext() : split the file extension (for reference)
# print(os.path.splitext(r'01_os.py'))
# ('01_os', '.py')

# File size in bytes (for reference)
# print(os.path.getsize('hello.json'))  # e.g., 204 bytes

# Absolute path (for reference)
# print(os.path.abspath('hello.json'))
# C:\MyCode\Python\hello.json




