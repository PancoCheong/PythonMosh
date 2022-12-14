# app.py
# for code quick test
from datetime import datetime, date
from sales1 import calc_tax, calc_shipping


def hello(person):
    print(f"Hello {person}, Good day, mate.")
    today = date.today()
    d_str = today.strftime("%Y-%b-%d")
    print("Today's date:", d_str)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print("         Now:", dt_string)


# output:
# Hello Panco, Good day, mate.
# Today's date: 2020-Apr-17
#          Now: 2020-04-17 13:58:11
hello('Panco')
#
# load customized module
calc_shipping()                 # output:calc_shipping
calc_tax()                      # output:calc_tax
