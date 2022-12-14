# --------------------------------------- ecommerce\shoppoing\__init__.py  ---------------------------------------
# 
# For relative imports to work in Python 3.6
import os
import sys
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


print(__name__, " package is loaded")
