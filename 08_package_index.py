# 08_package_index.py
#
# Python Package Index
# packages repository built by Python community
# https://pypi.org/
#
# search for "PDF"
#
# use pip to install (MacOS X or Linux use pip3)
#
# in terminal
#
### upgrade pip ###
# python -m pip install --upgrade pip
#
### package to post HTTP request ###
# pip install requests
#
# list of installed packages
# pip list
#
# 2     - major
# 23    - minor
# 0     - patch or bugfix
# requests          2.23.0
#
# search requests in pypi.org
# click Release History
# https://pypi.org/project/requests/#history
#
### install older version ###
# if latest have bug or incompatible with other packages
#
# install specified version
# pip install requests==2.22.0
#
# install latest compatible version (both commannds are the same)
# pip install requests==2.22.*  (latest version of 2.22.x)
# pip install requests~=2.22.0  (latest version of 2.22.x)
#
# pip install requests==2.*     (latest version of 2.x.x)
#
### remove packages ###
# pip uninstall requests
#
# scroll down to look for documentation for requests
# https://requests.readthedocs.io/en/latest/
#
# use it as module
#
#import requests
import requests

response = requests.get("http://google.com")
print(response)                 # output:<Response [200]>
#
#
# pip can only install single version of the same package
# if you need to use different version from the installed package
# you need to create a virtual environment
#
### virtual environment for package ###
# in terminal
# Linux and MacOS X, use python3
# by convention, name it 'env' folder
# python -m venv env
# VS code prompt:We noticed a new virtual environment has been created. Do you want to select it for the workspace folder?
#
# open ./env/pyvenv.cfg
# home = C:\Users\panco\AppData\Local\Programs\Python\Python38
# include-system-site-packages = false
# version = 3.8.2
#
# sub-folders: Include, Lib, Scripts (bin for MacOS X and Linux)
#
# activate the virtual environment
# for Windows: (run in command prompt, not in VS Code terminal)
# .env\Scripts\activate.bat
# for Linux and MacOS X:
# source env/bin/activate
#
# terminal will change as below, prefix by (env)
# (env) c:\repos\Python\Programmer\env\Scripts>
#
# install older package
# pip install requests==2.22.*
#
# check file: env\Lib\site-packages\requests\__version__.py
#
# deactivate
# env\Scripts\deactivate.bat
#
### pipenv ###
# better tools to set virtual environment
# pipenv - combined pip and virtual environment
# it is a Python equivalent tools as npm in node.js
#
# pip install pipenv
#
# delete the env folder, it is no longer needed
#
###  install package ###
# pipenv install requests
#
# it creates Pipfile, Pipfile.lock
# but, no env folder
#
### show the location of env ###
# output:C:\Users\panco\.virtualenvs\Programmer-b2xvsVMM
# pipenv --venv
#
# remove requests package from global
# pip uninstall requests
#
### run again ###
# output:ModuleNotFoundError: No module named 'requests'
# python .\08_package_index.py
#
# Python doesn't know the new virtual environment
# open command prompt
# c:\repos\Python\Programmer>pipenv shell
#
# output:<Response [200]>
# (Programmer-b2xvsVMM) c:\repos\Python\Programmer>python .\08_package_index.py
#
# (Programmer-b2xvsVMM) c:\repos\Python\Programmer> exit
#
#
### Virtual Environment in VS Code ###

