# 02_basic.py
# Python is case-sensitive
# Python use bytecode to achieve cross platform
# Python has serveral implmentation: offical python.org (cPython, written in C)
# other implementation: Jython (Java, allow import Java code),
# IronPython (C#, allow import C# code), Pypy (subset of Python)
# Python is dynamic typing language (like JS and Ruby), data type is determined at runtime,
# not at compile time like C#/Java/C++ that are static typing language

from string import Template
import string
import random
import math as m
### output to console ###
print("Panco")          # string can use double quote,  output:Panco
print('Single Quote')   # string can use single quote,  output:Single Quote
print('*-' * 5)         # repeat string 5 times,        output:*-*-*-*-*-
print(2+3)              # output result of expression,  output:5
print("a"+"b")          # concat 2 strings,             output:ab

### primitive basic type ###
students_count = 50     # int
rating = 4.95           # float
is_published = False    # bool
course_name = "Python"  # str
teacher_name = 'Panco'  # str
course_outline = """
Python support multiple lines string,
1st char and last char is newline character
"""                     # str, 1st and last character are newline
print(type(students_count))  # output:<class 'int'>
print(type(rating))  # output:<class 'float'>
print(type(is_published))  # output:<class 'bool'>
print(type(course_name))  # output:<class 'str'>
print(type(teacher_name))  # output:<class 'str'>
print(type(course_outline))  # output:<class 'str'>
# allow to change type in runtime (dynamic typing programming language like JavaScript and Ruby)
students_count = True
print(type(students_count))  # output:<class 'bool'>
print("-----")
# output: 1st line and last line is empty line (newline char)
print(course_outline)
print("-----")
# output: ignore 1st and last characters (ie. no newline char)
print(course_outline[1:-1])
print("-----")

# Python 3.6: type Annotation (linter: mypy can check this)
age: int = 40
age = True  # mypy linter at Python 3.8.2 is no longer check this incompatible types in assignment
print(age)  # output: True


my_list = [1, 2, 'a', True]         # allow different type
my_tuple = (1, 2, 'a', False)       # allow different type
my_dictionary = {'a': 1, 'b': 2}    # allow different type, key and value pair
# mutable - same memory address, add to add new item, output:[1, 2, 'a', True]
print(my_list)
# read-only version of list                         , output:(1, 2, 'a', False)
print(my_tuple)
# dictionary, like a data record, key and value pair, output:{'a': 1, 'b': 2}
print(my_dictionary)
print(type(my_list))        # output:<class 'list'>
print(type(my_tuple))       # output:<class 'tuple'>
print(type(my_dictionary))  # output:<class 'dict'>

# initialize  variable
x = 1
y = 2
print(f'x = {x}, y = {y}')  # output:x = 1, y = 2
# same as above 2 lines
# initialize multiple variables in a single line
x, y = 1, 2
print(f'x = {x}, y = {y}')  # output:x = 1, y = 2
# initialize multiple variables to same value
x = y = 1
print(f'x = {x}, y = {y}')  # output:x = 1, y = 1

# premitive basic data type is immutable, cannot change value
print("----- mutable and immutable type -----")
z = 1
# memory address of variable z,                                 output:140716671424160
print(id(z))
z = 2
# memory address of variable z is changed after new assignment, output:140716671424192
print(id(z))
# original memory address is subjected to garbage collection

my_list = [1, 2, 3]     # list are mutable
print(type(my_list))    # output:<class 'list'>
print(id(my_list))      # memory address of my_list,        output:2162985430976
my_list.append(4)
print(id(my_list))      # memory address remain the same,   output:2162985430976


### string ###
# len() - generic function to string or list
my_course = "Python for Programmer"
print(len(my_list))     # number of items, output:4
print(len(my_course))   # number of chars, output:21

print("----- string -----")
# string and print with format
# "string", 'string', '''multi-lines string'''
# string[0] - index (zero-base), -1 - index (backward from the end), string[m:n] - index range
# len(), upper(), lower(), find(), replace(), 'str' in my_string
# format string:
#  f'my_var = {my_var}'
#   'my name is %s, I have % 9.3f' % (my_name, my_amount)
#   '%%' - print %
#  print(i, end=" ") - replace newline with space
# \' - escape char, \\ - \, \n - newline
# \' - escape char, \\ - \, \n - newline
course = 'Python\' \\ \r\n "Tutorial"'
# output:
# Python' \
# "Tutorial"
print(course)
course = "Python\" %% 'Tutorial'"           # \" - escape char
print(course)                               # output:Python" %% 'Tutorial'
course = '''
Python's Tutorial
01.Introduction
02.Variable
03.String " and '
'''
print(course)                               # output: 1st line and last line is empty line (ie. newline)
print("----- string index -----")
print(course[1])        # ''' - 1st char and last char are newline, output:P
print(course[1:-1])     # exclude 1st char and last char,           output:no empty line at 1st and last
course = "   Python TutoriAl     "
#         01234567890123456789012
print(course[3])        # first index is 0 zero, output:P
print(course[-6])       # last char (from the back), output:l
# substring, start index to end index (exclude end position), output:Pyt
print(course[3:6])
print(course[4:])       # start index to the end, output:ython Tutorial
# first character to end index (exclude end position), output:   Pyth
print(course[:7])
print(course[:])        # output:   Python TutoriAl
### string function ###
print("----- string function -----")
print(len(course))          # length of string, output:23
# upper case,                       output:   PYTHON TUTORIAL
print(course.upper())
# lower case,                           output:   python tutorial
print(course.lower())
# 1st char of each word in upper case,  output:   Python Tutorial
print(course.title())
# 1st char is in upper case,            output:   python tutorial
print(course.capitalize())
# trim space, both begin and end,       output:Python TutoriAl
print(course.strip())
# trim space, begin only,               output:Python TutoriAl
print(course.lstrip())
# trim space, end only,                 output:   Python TutoriAl
print(course.rstrip())
print(course.find('t'))     # index of 1st char 't',    output:5
print(course.find('X'))     # return -1 if not found,   output:-1
# index of 1st char of 1st match word 'Tutor',          output:10
print(course.find('Tutor'))
# replace Python with Django, case sensitive,           output:   Django TutoriAl
print(course.replace('Python', 'Django'))  # original string doesn't change
print(course)  # output:   Python TutoriAl
# check if 'Python' in course string, output:True
print('Python' in course)
# check if 'Python' in course string, output:False
print('Python' not in course)

print("----- format string -----")
# without format string, use concat #
nickname = 'Panco'
familyname = 'Cheong'
message = nickname + ',(' + familyname + ')' + ' is programmer'
print(message)  # output:Panco,(Cheong) is programmer

# format string - evaluate expression #
message = f'{nickname},({familyname}) is programmer, lenght of {len(nickname)}, add = {4+5}'
print(message)  # output:Panco,(Cheong) is programmer, lenght of 5, add = 9

# format string #
# %c - character and ASCII code, %s - string
# %d - integer (in decimal format), %u - unsign integer
# %f - float, %e or %E - scientific number, %g or %G - scientific number
# %o - octal, %x - heximal, %X - heximal (upper case)
# %p - variable memory address (in hex)
amount = -123.1234567
# 12 characters in total, 3 decimal places precision,   output:    -123.123
print('%12.3f' % amount)
# the value of * is getting from the %(variable),       output:a=    -123.123
print("a=%*.*f" % (12, 3, amount))
print('%012.3f' % amount)   # prefix by zero,           output:-0000123.123
print('%-12.3f' % amount)   # align to the left,        output:-123.123

# algin + / - sign
print('%f' % amount)  # output:-123.123457
amount = amount * -1
print('%f' % amount)  # output:123.123457
print('%+f' % amount)       # display + sign            output:+123.123457
print('% f' % amount)       # display space for +       output: 123.123457
#  % (tuple),   output:My name is Panco, I have  +123.123 dollar
print('My name is %s, I have %+9.3f dollar' % (nickname, amount))

nHex = 0xFF
print("%%x nHex = %x,%%d nDec = %d, %%o nOct = %o" %
      (nHex, nHex, nHex))  # %% print single %, output:%x nHex = ff,%d nDec = 255, %o nOct = 377

# output:
# 0
# 1
# 2
for i in range(0, 3):
    print(i)
print("<-- newline by default")
# output:0 1 2
for i in range(0, 3):
    print(i, end=" ")
print("<-- use single space instead of newline")
# output:012
for i in range(0, 3):
    print(i, end="")
print("<-- use empty space instead of newline")

# format string
# https://www.cnblogs.com/nokiaguy/p/12100846.html
# use {} as place holder (subsitude in sequence)
print("a={}, b={}, c={}".format(1, 2, 3))  # output:a=1, b=2, c=3
# use {x} as named place holder
print("a={a}, b={b}, c={c}".format(c=3, a=1, b=2))  # output:a=1, b=2, c=3
# advance format
# output:original:中, use repr function:'中', Unicode'\u4e2d'.
print("original:{x!s}, use repr function:{x!r}, Unicode{x!a}.".format(x="中"))
# output:original:21.951234  float:21.951
print("original:{num}  float:{num:4.3f}".format(num=21.951234))
# output:decimal:56  binary:111000  octal:70  heximal:38
print("decimal:{n}  binary:{n:b}  octal:{n:o}  heximal:{n:x}".format(n=56))
# output:scientific number:5.330000e+02
print("scientific number:{num:e}".format(num=533))
# 3 integer, 2 decimal places, output:percentage:56.12%
print("percentage:{num:3.2%}".format(num=0.561234))
# prefix 0, output:chapter-04
print("chapter-{chapter:02.0f}".format(chapter=4))
# prefix 0, output:chapter-11
print("chapter-{chapter:02.0f}".format(chapter=11))

# number is 10 digits and 4 decimal places
# < - align to left, ^ - align to center, > - align to right
# output:
# 12345.7890
# 1.1200
#  2.1200
#    3.1200
print('{:10.4f}\n{:<10.4f}\n{:^10.4f}\n{:>10.4f}'.format(
    12345.7890, 1.12, 2.12, 3.12))
# display ^ between - sign and number, output:-^^^^^5.43
print("{0:^=10.2f}".format(-5.43))

### Exercise - format string acts like a message template ###
formatString = "Hello %s. Today is %s, Are there any activities today?"
values1 = ("Panco", "Sunny day")    # tuple data type
values2 = ("Amy", "Windy day")      # tuple data type
# output:Hello Panco. Today is Sunny day, Are there any activities today?
print(formatString % values1)
# output:Hello Amy. Today is Windy day, Are there any activities today?
print(formatString % values2)

# use Template in string module
# from string import Template
# $s and ${s} are the same, but ${s} is easier to read, $$ - escape for $
template = Template("$s,Python. ${s},Django. Get good $$")
# output:Hello,Python. Hello,Django. Get good $
print(template.substitute(s="Hello"))

# international Currency sign, \uXXXX to input unicode character
# https://www.fileformat.info/info/unicode/category/Sc/list.htm
# U+0024	DOLLAR SIGN	            $
# U+00A3	POUND SIGN	            £
# U+00A5	YEN SIGN	            ¥
# U+20A9	WON SIGN	            ₩
# U+20A0	EURO-CURRENCY SIGN	    ₠
template2 = Template(
    "Exchange rate@${date_string}: ${sign1}${currency1} is equivalent to ${sign2}${currency2}")
data = {}       # use dictionary as a data record
data['date_string'] = '2020-04-11'
data['sign1'] = '\u0024'
data['currency1'] = 1.24
data['sign2'] = '\u00A3'
data['currency2'] = 1.00
# output: {'date_string': '2020-04-11', 'sign1': '$', 'currency1': 1.24, 'sign2': '£', 'currency2': 1.0}
print(data)
# output:Exchange rate@2020-04-11: $1.24 is equivalent to £1.0
print(template2.substitute(data))
data['date_string'] = '2020-04-11'
data['sign1'] = '\u0024'
data['currency1'] = 0.9145
data['sign2'] = '\u20A0'
data['currency2'] = 1.00
# output:{'date_string': '2020-04-11', 'sign1': '$', 'currency1': 0.9145, 'sign2': '₠', 'currency2': 1.0}
print(data)
# output:Exchange rate@2020-04-11: $0.9145 is equivalent to ₠1.0
print(template2.substitute(data))

### numbers ###
print("----- Numbers -----")
d = 10              # decimal: 10
b = 0b10            # binary: 10 --> dec: 2
print(b)            # display in decimal value,     output:2
print(bin(b))       # display in binary value,      output:0b10
o = 0o127           # octal: 127    (64*1->64, 8*2->16, 7->7)
print(o)            # display in decimal value,     output:87
print(oct(o))       # display in octal value,       output:0o127
# heximal: 12c --> 1->256(16**2*1),2->32(16**1*2),c->12(16**0*12)
x = 0x12c           # 256+32+12 = 300
print(x)            # display in decimal value,     output:300
print(hex(x))       # displah in heximal value,     output:0x12c

### complex number a + bi = a,b is real number, i is imaginary unit###
x = 1 + 2j          # j or J for imaginary unit in Python
y = 1 + 2J          # store in lower case
print(y)            # complex number,               output:(1+2j)


print("----- arithmetic -----")
# operators: + - * ** / // %

print(10 + 3)       # add,              output:13
print(10 - 3)       # minus,            output:7
print(10 * 3)       # multiply,         output:30
print(10 ** 3)      # exponent, 10 to the power of 3, output:1000
print(10 / 3)       # divide,     float output:3.3333333333333335
print(-10 / 3)      # divide,     float output:-3.3333333333333335
# floor division: round down to near integer, smaller in value
print(10 // 3)      # floor division,   output:3
print(-10 // 3)     # floor division,   output:-4
print(10 % 3)       # modulus,          output:1
print(-10 % 3)      # modulus,          output:2

### assignment ###
print('----- assignment -----')
PI = 3.14159        # use upper case to name constant, Python has no const keyword
x = 10
x = x + 3
print(x)            # output:13
x += 3              # augmented assignment, but no x++ in Python
print(x)            # output:16
x -= 3              # augmented assignment, but no x-- in Python
print(x)            # output:13
x *= 3              # augmented assignment
print(x)            # output:39
x /= 3              # augmented assignment
print(x)            # output:13.0
print('----- operator precedence -----')
# 1. parenthesis
# 2. exponentiation 10 ** 3
# 3. multiplication or division
# 4. addition or substraction
x = 10 + 3 * 2
print(x)                # output:16
x = 10 + 3 * 2 ** 2
print(x)                # output:22
x = (2 + 3) * 10 - 3
print(x)                # output:47

# Python 3 built in functions
# https://docs.python.org/3/library/functions.html

# Python math module
# https://docs.python.org/3/library/math.html

### math ###
print('----- function in math module -----')
x = 12.950000
y = -12.950000
print(round(x))         # round to integer,     output:13
print(round(x, 1))      # round to 1 digit,     output:12.9
print(round(y, 1))      # round to 1 digit,     output:-12.9
print(abs(y))           # absolute value,       output:12.95
# require import math module
# Python 3 math module
# https://docs.python.org/3/library/math.html
# import math as m
print(m.ceil(x))        # ceiling,              output:13
print(m.ceil(y))        # ceiling,              output:-12
print(m.floor(x))       # floor,                output:12
print(m.floor(y))       # floor,                output:-13
print(m.trunc(x))       # truncate,             output:12
print(m.isnan(x))       # is not a number,      output:False
print(m.sqrt(x))        # square root,          output:3.598610843089316
print(m.remainder(10, 3))    # remainder,       output:1.0
print(m.remainder(-10, 3))   # remainder,       output:-1.0


### type conversion ###
print('----- type conversion -----')
# get input
name = input('What is your name? ')
print('Hi ' + name)  # concat string,           output:Hi Aidan

### Type conversion: int(x) float(x) bool(x) str(x)###
# input() is string
# input: 2005
birth_year = input('Birth year: ')
print(type(birth_year))  # output:<class 'str'>
# convert string to integer
age = 2020 - int(birth_year)
print(age)  # output:5
print(type(age))  # output:<class 'int'>

# convert lbs to kg
lbs_to_kg = 0.45359237
lbs_string = '200.5'
kg = float(lbs_string) * lbs_to_kg
print(kg)  # output:90.945270185

# Type conversion
x = 1
print("value of 1:")
print(int(x))           # integer,  output:1
print(float(x))         # float,    output:1.0
print(bool(x))          # boolean,  output:True
print(str(x))           # string,   output:1
# Falsy value: 0, "" - empty string, [] - empty list
# None - empty value (null in other language)
# () - empty tuple, {} - empty dictionary
# value other than Falsy value is True
print('--- test falsy value ---')
print(bool(0))                  # zero,             output:False
print(bool(-1))                 # non-zero,         output:True
print(bool(""))                 # empty string,     output:False
print(bool("   "))              # space string,     output:True
print(bool("False"))            # non-empty string, output:True
print(bool([]))                 # empty list,       output:False
print(bool([1, 2, "a", "b"]))   # non-empty list,   output:True
print(bool(None))               # null value,       output:False
print(bool(()))                 # empty tuple,      output:False
print(bool({}))                 # empty dictionary, output:False


print("----- conditional statement -----")
# condition: if bool:    elif bool:    else:
# intention is a code block, no {}

# Falsy value - " " space is not False
name = " "
if not name.strip():
    # trim space becomes empty -> False, output:Name is empty!
    print("Name is empty!")
# condition
age = 21
if age >= 18 and age < 65:
    print("Go to work")         # output:Go to work
# re-write above, easier to read
if 18 <= age < 65:
    print("Go to work again")   # output:Go to work again
# Ternary Operator
if age >= 18:
    message = "Go to Work"
else:
    message = "Enjoy life"
print(message)                  # output:Go to Work
# re-write above condition
# in C# / Java
# message = age >= 18 ? "Go to work": "Enjoy life"
# in Python
message = "Go to work again" if age >= 18 else "Enjoy life again"
print(message)                  # output:Go to work again

# output:
# It's a lovely day
# Enjoy your day
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
elif is_hot and not is_cold:
    pass  # empty code block, use pass keyword
else:
    print("It's a lovely day")
print("Enjoy your day")


# and, or, not
has_high_income = False
has_good_credit = True
has_criminal_record = False
# AND,  output:None
if has_high_income and has_good_credit:
    print("Eligible for loan with lower down payment")
# OR,   output:Eligible for loan with higher down payment
if has_high_income or has_good_credit:
    print("Eligible for loan with higher down payment")
# NOT,  output:Eligible for loan, no criminal record
if has_good_credit and not has_criminal_record:
    print("Eligible for loan, no criminal record")
# logical operator: > < <= >= == !=

# output:It's a cold day
temperature = 4
if temperature >= 30:
    print("It's a hot day")
elif temperature <= 10:
    print("It's a cold day")
else:
    print("It's a nice day")

### exercise ###
# input:200, L
# output:90.72 kilos
weight = float(input("Input your weight: "))
unit = input("(L)bs or (K)g: ")[0]
kg_to_lbs = 2.2046226218488
if unit.upper() == 'L':
    output = weight / kg_to_lbs
    print('%.2f kilos' % (output))
else:
    output = weight * kg_to_lbs
    print('%.2f pounds' % (output))

print("----- for loop -----")
# for loop
# output:
# A
# B
# C
for x in "ABC":          # string
    print(x)
# output: a b c
for x in ['a', 'b', 'c']:
    print(x, end=" ")
# output: 2 3 4
for x in range(2, 5):       # print 2 to 5, range object
    print(x, end=" ")
# output: 0 2 4 6 8
for x in range(0, 10, 2):   # step=2, print even numbers, range object
    print(x, end=" ")

print(range(5))             # range is not a list, output:range(0, 5)
# range class, small footprint in memory eg. range(99999999)
print(type(range(5)))           # output:<class 'range'>
print([1, 2, 3, 4, 5])          # a list, output:[1, 2, 3, 4, 5]
print(type([1, 2, 3, 4, 5]))    # output:<class 'list'>

### for else code block ###
# Python doesn't need to use is_found flag to control not found logic
# output:Found: Amy
names = ["Panco", "Amy", "Sophy", "Aidan"]
#is_found = False
for name in names:
    if name.startswith("A"):
        print(f"Found: {name}")
#        is_found = True
        break
else:
    print("Name start with 'A' is not found")
# if not is_found:
#    print("Name start with 'A' is not found")


# while loop - use pass keyword for empty code block
print("----- while loop -----")
# output:
# *
# **
# ***
# ****
# *****
# Done
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

### exercise ###
# input:1, 2, 3
# output:
# Incorrect
# You won!
# import random
secert_number = random.randint(1, 9)
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    input_number = int(input("Guess a number (1 - 9):"))
    if input_number == secert_number:
        print("You won!")
        break
    elif input_number == 0:
        continue
    else:
        print("Incorrect")
    guess_count += 1
else:   # execute when while condition is false
    print("You lost!")

### ------ Exercise - data validation ------ ###
data_valid = False
while data_valid == False:
    number1 = input("Input a number (1 - 9):")

    try:
        number1 = int(number1)  # dynamic typing, change type
    except:
        print("Invalid input. Only numbers are accepted")
        continue

    if number1 < 1 or number1 > 9:
        print("The number must be between 1 to 9")
        continue
    else:
        data_valid = True

print("number 1 =", number1)


### random ###
#import random
# generate random integer number between 1 to 10,   eg. output:4
print(random.randint(1, 10))
# generate random float number between 0 to 1,      eg. output:0.003671148062525331
print(random.random())
# generate random float number between 1.1 to 5.4,  eg. output:3.4245019179658347
print(random.uniform(1.1, 5.4))
# random pick a character,                          eg. output:h
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))
# random ODD number between 1 to 100 (step +2),     eg. output:81
print(random.randrange(1, 100, 2))
# random EVEN number between 1 to 100 (step +2),    eg. output:74
print(random.randrange(0, 101, 2))
# random pick 5 characters,                         eg. output:['f', 'b', 'p', 'q', 'c']
print(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
#import string
# random pick 8 characters from letters and digits, eg. output:AZba3Isx
# ''.join - combine the values in list into string
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)

a = [1, 3, 5, 6, 7]
random.shuffle(a)	    # shuffle the list,         eg. output:[6, 7, 5, 1, 3]
print(a)

print(random.choice(['剪刀', '石头', '布']))  # unicode support, eg. output:布


### exercise - game command ###
# input: start, stop, quit
# output:
# game is started... ready to play!
# game is stopped.
# bye.
command = ""
help_content = '''
start - to start the game
stop - to stop the game
quit = to exit
'''
while command.lower() != "quit":
    command = input("command>").lower()
    if command == 'help':
        print(help_content[1:-1])  # ignore 1st and last newline
    elif command == 'start':
        print("game is started... ready to play!")
    elif command == 'stop':
        print("game is stopped.")
    elif command == 'quit':
        print("bye.")
        break
    else:
        print("I don't understand that...")


print("----- self-defined functions -----")
# basic syntax
# pass - empty code block
# formatter will add 2 empty after each function
# always return value: return None by default


def my_func(my_param_list):
    pass


def increment(number, by):
    return number + by


print(my_func(5))       # print, output:None
print(increment(2, 3))  # print, output:5

# return multiple values thru tuple - read-only list


def add(num1=1, num2=2):  # set default value of parameter
    return (num1, num2, num1 + num2)


# keyword argumnet - use name to specify parameter
print(add(num2=4))        # print tuple, output:(1, 4, 5)


# type annotation for parameters and return value
def minus(num1: int = 1, num2: int = 2) -> tuple:
    return (num1, num2, num1 - num2)

# Open debugger: Ctrl + Shift + D


def multiply(*list):  # pass in variable number of parameters, *var means tuple
    total = 1
    for number in list:
        total *= number
    return total


print("start debugging")
print(multiply(1, 2, 3, 4))         # output:24
print(multiply(1, 2, 3, 4, 5, 6))   # output:720
print("finish")


def save_user(**user):  # **var means dictionary, like an object in Javascript
    print(user)         # dict, output:{'id': 1, 'name': 'Panco'}


save_user(id=1, name="Panco")

print("----- Scope -----")
# two types of variables in Python
# 1. local variables with the function scope - only can access within function
# 2. global variables with the file scope
### Python doesn't have block level scope ###

my_value = "a"
my_global_value = "x"


def greet():
    # although my_value is global variable,
    # Python create a local variable with the same name inside function
    # to avoid changing the value in global scope by default
    my_value = "b"
    # do not create local variable, directly refer to global variable
    # avoid to use global - may have side effect on other function that use the same variable
    global my_global_value
    my_global_value = "y"
    if True:
        my_message = "This is function scope variable"
    # can access outside above code block
    print(my_message)           # output:This is function scope variable
    print(my_value)             # output:b
    print(my_global_value)      # output:y


greet()
# print(my_message)             # cannot access function variable
print(my_value)                 # output:a
print(my_global_value)          # output:y

# type any letter of the keyword: intelli-sense auto-complete is still able to pick it up
# eg. type
# mgv ----> my_global_value

### exercise ###
# Fizz and Buzz
# divisible by 3: Fizz
# divisible by 5: Buzz
# divisible by 3 and 5: FizzBuzz
# others: display the input value

# no need elif, return will only run one of the statement
# no need else, as the last statement will only execute if no match


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))     # output:Fizz
print(fizz_buzz(6))     # output:Fizz
print(fizz_buzz(5))     # output:Buzz
print(fizz_buzz(10))    # output:Buzz
print(fizz_buzz(15))    # output:FizzBuzz
print(fizz_buzz(30))    # output:FizzBuzz
print(fizz_buzz(7))     # output:7
print(fizz_buzz(11))    # output:11
