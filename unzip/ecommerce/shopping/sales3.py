# 06_module
# folder: ecommerce\shopping
# --------------------------------------- sales3.py  ---------------------------------------
from ecommerce.customer import contact

print(__name__, " module is initialized")
#
#
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
#
# ecommerce/shopping/sales_module3.py
# convention: all lower cases and _
#
### absolute import ###
# output: ModuleNotFoundError: No module named 'ecommerce'

# output: contact_customer
#
### relative import ###
# output: ImportError: attempted relative import with no known parent package
#from ..customer import contact
# contact.contact_customer()            # output:contact_customer


def calc_tax():
    print("calc_tax 3")
    contact.contact_customer()


def calc_shipping():
    print("calc_shipping 3")
