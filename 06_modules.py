# 06_modules.py

# 1. Packages or modules provided by Python itself (official)
# 2. Packages or modules we write ourselves (custom)
# 3. Packages or modules written by others: third-party packages or modules

# install to Global vs Virtual Environment
# - Global installation: packages are installed system-wide and available to all projects (by default)
#        pip install package_name
# - Virtual environment (venv): creates isolated environments for each project, preventing conflicts between package versions
#        1. cd path/to/your/project
#        2. python -m venv myenv
#        3. (Mac zsh/Linux bash): source myenv/bin/activate    # (Windows): myenv\Scripts\activate
#        4. pip install package_name
#        5. deactivate   (exit venv)
#
# Installing third-party packages
#  1. Install via PyCharm settings
#  2. Try importing the package; if you get an error, hover over the name and follow the installation prompt
#  3. Install via command line (important, recommended):
#       pip install numpy        # install a package
#       pip uninstall numpy      # uninstall a package
#       pip show numpy           # view package details
#       pip list                 # view all packages
#       pip freeze               # view only packages you installed (with version numbers)

#       pip freeze > requirements.txt       # export current environment packages to requirements.txt
#       pip install -r requirements.txt     # install packages listed in requirements.txt

#    If installation is slow, try switching to a different mirror:
#       pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

#   Set a permanent mirror:
#       pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

import requests
import numpy as np
import pandas as pd

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # matplotlib

import flask
import tornado
'''

''' '''

import math

# Package: a folder that contains an __init__.py file
# Module: a single Python file
#
# Encapsulation idea: Project => Package (folder) => Module (Python file) => Class => Function => Code
#
#Create a module file named module1.py in current folder
myvar1 = "name variable in module 1"
print('I am module1')

def fn1(n=3):
    print("function fn1 in module1", n**2)
#
# Create a package
# Create a folder named "package1"
# Inside "package1" folder: 
#       - Create an empty file named __init__.py
#
#       - Create a module file named module2.py
myvar2 = "name variable in module 2"
print('I am module2')

def fn2(n=3):
    print("function fn2 in module2", n**2)

#
# Import modules
#   import my_module
#   from my_package import my_module

# import time, math, random (official modules)
import math
import random
#
# Imports the entire time module. You must prefix functions with the module name.
import time
time.sleep(0.1)
#
# Imports only the sleep function from the time module. You can directly call sleep() without the module name.
from time import sleep
sleep(0.1)
#
# Wildcard import: Imports all public names (functions, classes, variables) from time into the current namespace.
# Avoid from module import * except for quick tests or interactive sessions.
# Risky: name clashes, less readable 
from time import *
print(time())
print()
#


# Custom modules: modules are singleton (importing multiple times still uses the same instance)
'''
import module1
import module1

print(module1.myvar1)
module1.fn1()
'''

# Import specific items from a module (ie. myvar1 variable and fn1 function)
'''
from module1 import myvar1, fn1
print(myvar1)
# print(module1.myvar1)  # Error
fn1()
'''


# Module inside a package
'''
# from package1 import module2
# print(module2.myvar2)

from package1.module2 import myvar2
print(myvar2)
'''


# Alias: after renaming with "as", you can only use the alias
import module1 as m1
print(m1.name)

from package1 import module2 as m2
print(m2.name)




#
# just like find a product in supermarket
# if supermarket doesn't have isles, sections or departments for highly related products.
# it is even harder to find the product that you want
#
# a program code for production could have 10000+ lines of code,
# we don't want to write all 10000+ code in a single file
# it is hard to find, troubleshoot and maintain
# we should split our code across multiple files.
#
# in Python, each file is a module, that contains some Python code
#
# How do we decide which classes, methods or variables we should put in what modules?
# each module should contain highly related objects

# put below two methods in separate file named:
# sales1.py
# module name by convention: all lower cases and _
#
# def calc_tax():
#     print("calc_tax")

# def calc_shipping():
#     print("calc_shipping")
#
# add print() in module and __init__ package files
# output:
# ecommerce  package is loaded
# ecommerce.customer  package is loaded
# ecommerce.customer.contact  module is initialized
# ecommerce.shopping  package is loaded
# ecommerce.shopping.sales3  module is initialized
# ecommerce.sales2  module is initialized
# sales1  module is initialized
from ecommerce.customer import contact
from ecommerce.shopping import sales3
import ecommerce.sales2 as sales2
import sys
from sales1 import calc_shipping, calc_tax      # use , for multiple import
import sales1
import sales1 as s

# output:__main__  module is initialized
print(__name__, " module is initialized")

### using module ###
# 1. import specific items
# use , for multiple import
# from sales1 import calc_shipping, calc_tax
#
# use it as they are defined locally
calc_shipping()             # output:calc_shipping
calc_tax()                  # output:calc_tax
#
# easier way to use *, but it is a bad practice
# current module and imported module may have same class or method,
# which causes conflict
# from sales1 import *
#
#
### 2. import entire module ###
# import sales1
#
sales1.calc_tax()     # output:calc_tax
#
#
# import sales1 with alias
# import sales1 as s
s.calc_tax()            # output:calc_tax
#
#
#
### compiled Python files ###
#
# in termial:
# python 06_modules.py
#
# cd __pycache__
#
# compiled version of module
# sales1.cpython-38.pyc
#
# if Python interpreter see the compiled version of import module
# it loads that module automatically without the need of re-compile them
#
# Python will check the datetime between .py and .pyc
# to see if the compiled module is up-to-date, recompile if out-dated
#
# Python always recompiles the module that we load directly from the commmand line.
# ie. 06_modules.py, so no compiled file will be generated
#
#
### Module search path ###
#
# Python search the module
# 1. sales1.py in current folder
# 2. follow Python search path
#
# print the list of folders that Python will look for files
# output:
# ['c:\\repos\\Python\\Programmer', 'C:\\Users\\panco\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\panco\\AppData\\Local\\Programs\\Python\\Python38\\DLLs',
# 'C:\\Users\\panco\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\panco\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\panco\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\panco\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
#
# Python search path:
# formatted output:
# ['c:\repos\Python\Programmer', # current folder
#  'C:\Users\panco\AppData\Local\Programs\Python\Python38\python38.zip',
#  'C:\Users\panco\AppData\Local\Programs\Python\Python38\DLLs',
#  'C:\Users\panco\AppData\Local\Programs\Python\Python38\lib',
#  'C:\Users\panco\AppData\Local\Programs\Python\Python38',
#  'C:\Users\panco\AppData\Roaming\Python\Python38\site-packages',
#  'C:\Users\panco\AppData\Local\Programs\Python\Python38\lib\site-packages']
#
# import sys
print(sys.path)
#
#
### package ###
# import module from folder or sub-folder
# package is a container for one or more modules
# package is mapped to folder
#
# if the program becomes large, it is better to organize the module into folder or sub-folder
#
# create ecommerce and copy the sales1.py to it
# rename it as sales2.py
# ./ecommerce/sales2.py
#
# in ecommerce folder
# add file: __init__.py (with empty content)
# then Python will treat this folder as a package
# the folder may contain multiple files (modules)
#
#
# type the full name for each method call is a bit too long
# import ecommerce.sales2
# ecommerce.sales2.calc_tax()        # output:calc_tax 2
#
# you may use alias
#import ecommerce.sales2 as sales2
sales2.calc_tax()                           # output:calc_tax 2
#
# or use 'from' statement
# from ecommerce.sales2 import calc_tax
# calc_tax()                                # output:calc_tax 2
#
# from ecommerce import sales2
# sales2.calc_tax()
#
#
### sub-package ###
# from ecommerce.shopping import sales3
sales3.calc_tax()                    # output:calc_tax 3
#
#
### intra-package reference ###
# either use absolute or relative import statement
#
# output:
# calc_tax 3
# contact_customer
sales3.calc_tax()                    # output:calc_tax 3
#
#
#
### dir function ##
# list all attributes and methods
#
# output:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax', 'contact']
print(dir(sales3))
#
#
# output:Module 'ecommerce.shopping.sales3' has no '__builtins__' member
# print('cached: ', sales3.__builtins__)

# output:cached:  c:\repos\Python\Programmer\ecommerce\shopping\__pycache__\sales3.cpython-38.pyc
print('cached: ', sales3.__cached__)     # output:None
# output:doc:  None
print('doc: ', sales3.__doc__)
# output:file:  c:\repos\Python\Programmer\ecommerce\shopping\sales3.py
print('file: ', sales3.__file__)
# output:loader:  <_frozen_importlib_external.SourceFileLoader object at 0x000001F52EA14790>
print('loader: ', sales3.__loader__)
# output:name:  ecommerce.shopping.sales3
print('name: ', sales3.__name__)
# output:package:  ecommerce.shopping
print('package: ', sales3.__package__)
# output:spec:  ModuleSpec(name='ecommerce.shopping.sales3', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001F52EA14790>, origin='c:\\repos\\Python\\Programmer\\ecommerce\\shopping\\sales3.py')
print('spec: ', sales3.__spec__)
#
#
### executing modules as script ###
# statement in module will execute at the first time when the module is loaded
# the module will then cached in memory
#
# add print() in ecommerce.shopping.sales3
# output:ecommerce.shopping.sales3 is loaded
#
# add print() in __init__.py
#
# module that call by python.exe directly always has name '__main__'
# this module will always recompile by Python, never load from .pyc
# output:__main__  module is initialized
print(__name__, " module is initialized")
#
#
# we can kick start the program by the following code
# as only the direct involved .py has the __main__ module name
# even this code existed in other module, it will not be executed
if __name__ == "__main__":
    print("Sales started")
    calc_tax()



