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
# show the info of installed package
# pip show requests
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
from pancopackage import mymodule, myanothermodule
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
# but, no env folder, the virtual environment is created in separated folder
# reason for this is to keep the project files size small
#
### show the location of env ###
# home laptop output:C:\Users\panco\.virtualenvs\Programmer-b2xvsVMM
# company PC output:C:\Users\panco.cheong\.virtualenvs\PythonMosh-OI8O7wJw
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
# open command prompt (not in VS terminal)
# c:\repos\Python\Programmer>pipenv shell
#
# output:<Response [200]>
# (Programmer-b2xvsVMM) c:\repos\Python\Programmer>python .\08_package_index.py
#
# (Programmer-b2xvsVMM) c:\repos\Python\Programmer> exit
#
#
### Virtual Environment in VS Code ###
# run the code in VS code
# output:ModuleNotFoundError: No module named 'requests'
# how to tell VS code the use virtual env
#
# in terminal
# pipenv --venv
# output:C:\Users\panco\.virtualenvs\Programmer-b2xvsVMM
#
# review the folder structure
# explorer C:\Users\panco\.virtualenvs\Programmer-b2xvsVMM
#
# https://code.visualstudio.com/docs/python/environments
#
# get the path and add \Scripts\python.exe
# C:\Users\panco.cheong\.virtualenvs\PythonMosh-OI8O7wJw\Scripts\python.exe
#
# if you are using code-runner extension
# Preferences --> Settings (Ctrl+,)
# search Edit in Settings.json
# in below section, replace the value of "python" key with
# "code-runner.executorMap":
# "python": "C:\Users\panco.cheong\.virtualenvs\PythonMosh-OI8O7wJw\Scripts\python.exe"
#
# https://code.visualstudio.com/docs/python/environments
#
# open .vscode\settings.json
# "python.pythonPath": "C:\\Users\\panco.cheong\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
#
# restart the VS code, it will able to lookup the venv in  Python: Select Interpreter
# change the Interpreter
# VS code prompts to install pylint and autopep8 for this venv
#
#
#### pipfile and pipfile.lock ###
# keep track of the dependency of the project
#
# pipfile
#
# [[source]]                    # packages download from
# name = "pypi"
# url = "https://pypi.org/simple"
# verify_ssl = true

# [dev-packages]                # packages only for development
# pylint = "*"
# autopep8 = "*"

# [packages]                    # packages that the project depends on
# requests = "*"                # * means latest version

# [requires]                    # requires python version to run this application
# python_version = "3.8"
#
#
# pipfile.lock - the exact version detail of each package
#
# detail for [packages] --> default section
# "default": {
#     "certifi": {
#         "hashes": [
#             "sha256:1d987a998c75633c40847cc966fcf5904906c920a7f17ef374f5aa4282abd304",
#             "sha256:51fcb31174be6e6664c5f69e3e1691a2d72a1a12e90f872cbdb1567eb47b6519"
#         ],
#         "version": "==2020.4.5.1"
#     },
#     "requests": {
#         "hashes": [
#             "sha256:43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee",
#             "sha256:b3f43d496c6daba4493e7c431722aeb7dbc6288f52a6e04e7b6023b0247817e6"
#         ],
#         "index": "pypi",
#         "version": "==2.23.0"
#     },

# detail for [dev-packages] --> develop section
# "develop": {
#     "astroid": {
#         "hashes": [
#             "sha256:71ea07f44df9568a75d0f354c49143a4575d90645e9fead6dfb52c26a85ed13a",
#             "sha256:840947ebfa8b58f318d42301cf8c0a20fd794a33b61cc4638e28e9e61ba32f42"
#         ],
#         "version": "==2.3.3"
#     },
#     "autopep8": {
#         "hashes": [
#             "sha256:152fd8fe47d02082be86e05001ec23d6f420086db56b17fc883f3f965fb34954"
#         ],
#         "index": "pypi",
#         "version": "==1.5.2"
#     },
#
#
# this info is used to recreate the virtual environment if we change the PC
#
# delete the virtual environment folder
# pipenv --venv
#
# Windows: rmdir /s /q "C:/Users/panco.cheong/.virtualenvs/PythonMosh-OI8O7wJw"
# MacOS X: rm -rf /Users/panco.cheong/.virtualenvs/PythonMosh-OI8O7wJw
#
# output: No virtualenv has been created for this project yet!
# pipenv --venv
#
# reinstall the venv
# pipenv install
#
# as requests = "*"  # specify the latest version
# if you want to install the exact version stated in pipfile.lock
# pipenv install --ignore-pipfile
#
#
### manage dependencies ###
# show all dependencies
# pipenv graph
#
# uninstall package
# pipenv uninstall requests
#

#
# install package with specified version
# pipenv install requests==2.9.*
#
# pipfile
# [packages]
# requests = "==2.9.*"
#
# pipfile.lock
# "requests": {
#     "hashes": [
#         "sha256:22a8c72dfc7fc18db1aca6784e97a638e9d09abe2cd387be473f88bd6dcba22f",
#         "sha256:d8be941a08cf36e4f424ac76073eb911e5e646a33fcb3402e1642c426bf34682"
#     ],
#     "index": "pypi",
#     "version": "==2.9.2"
# }

### find the outdated packages ###
# it shows the yellow warning
# output:Skipped Update of Package requests: 2.9.2 installed, 2.23.0 available.
# pipenv update --outdated
#
# requests package cannot be upgraded because pipfile requests = "==2.9.*"
# change requests = "==2.*"
# run again
# the yellow warning is gone as 2.* is compatible with 2.23.0
# output:Package 'requests' out-of-date: '==2.9.2' installed, '==2.23.0' available.
# pipenv update --outdated
#
### update the package ###
# pipenv update requests
#
# pipfile.lock
# "requests": {
#     "hashes": [
#         "sha256:43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee",
#         "sha256:b3f43d496c6daba4493e7c431722aeb7dbc6288f52a6e04e7b6023b0247817e6"
#     ],
#     "index": "pypi",
#     "version": "==2.23.0"
# },
#
#
### register account in pypi.org ###
# hotmail
# R@lli<car>
##

### publish package to pypi.org ###
### install 3 packages ###
# pip install setuptools wheel twine
#
#from pancopackage import mymodule, myanothermodule

myanothermodule.displaymessage()
# display = mymodule.displaymessage()
# mymodule.displaymessage()
#
### view the documentation of math module ###
# pydoc math
# pydoc pancopackage
#
### convert document to HTML ###
# pydoc -w pancopackage.mymodule
#
# host the document in web server
# -p - port number
# pydoc -p 8080
