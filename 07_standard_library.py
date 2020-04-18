# 07_standard_library
# folder: .
# --------------------------------------- 07_standard_library.py  ---------------------------------------
# topics: files, SQLite, Date Time, Random Values, Emails
#
import subprocess
import sys
from email.mime.image import MIMEImage
from string import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import string
import secrets
import random
from datetime import datetime, timedelta
import time         # time stamp
import sqlite3
import json
import csv
from zipfile import ZipFile
import shutil
from time import ctime
from pathlib import Path

### Path ###
# google search: https://docs.python.org/3/library/pathlib.html
#
# from pathlib import Path
#
# Absolute Path
#
# path in Windows
Path("C:\\repos\\Python\\MyFolder")
#
# use Raw string - no escape char
Path(r"C:\repos\Python\MyFolder")
#
# path in MacOS or Linux
Path("/repos/Python/MyFolder")
#
# Current Folder
Path()
#
# relative path
Path(r"ecommerce\__init__.py")
#
# Combined the paths
Path() / Path("ecommerce") / Path("__init__.py")
#
# Home folder for current user
Path.home()
#
# working with path
path = Path(r"ecommerce\__init__.py")
print(path.exists())    # is exist, output:True
print(path.is_file())   # is file, output:True
print(path.is_dir())    # is directory, output:False
print(path.name)        # filename, output:__init__.py
print(path.stem)        # filename without extension, output:__init__
print(path.suffix)      # file extension, output:.py
print(path.parent)      # parent folder, output:ecommerce
# absolute path, output:C:\repos\Python\Programmer\ecommerce\__init__.py
print(path.absolute())

#
path = path.with_name("newfile.txt")
print(path)             # change file.ext, output:ecommerce\newfile.txt
path = path.with_suffix(".py")
print(path)             # change .ext, output:ecommerce\newfile.py
#
#
### directory ###
path = Path("NewFolder")
path_new = Path("NewFolderName")
if not path.exists():
    path.mkdir()                                # create new folder
    # output:NewFolder is created
    print(path, "is created")
#
if path.exists() and not path_new.exists():
    path.rename("NewFolderName")                # rename folder
    # output:NewFolder  is renamed to  NewFolderName
    print(path, " is renamed to ", path_new)
#
if path_new.exists():
    path_new.rmdir()                            # remove folder
    # output:NewFolderName is removed
    print(path_new, "is removed")
#
# iterate folder - generator object
# output:<generator object Path.iterdir at 0x000001A2D214D740>
# return a value on every time it iterate (not to store all data in memory)
print(path.iterdir())
#
# list of files and folders in path (non-recursive to sub-folder)
# output:
# ecommerce\customer
# ecommerce\sales2.py
# ecommerce\shopping
# ecommerce\__init__.py
# ecommerce\__pycache__
path = Path("ecommerce")
for p in path.iterdir():
    print(p)
#
# use list comprehension
# convert generator to list
#
paths = [p for p in path.iterdir()]
# output:[WindowsPath('ecommerce/customer'), WindowsPath('ecommerce/sales2.py'), WindowsPath('ecommerce/shopping'), WindowsPath('ecommerce/__init__.py'), WindowsPath('ecommerce/__pycache__')]
# PosixPath in MacOS X and Linux, Posix is the filesystem standard use in Unix like OS
print(paths)

folders = [p for p in path.iterdir() if p.is_dir()]
# output:[WindowsPath('ecommerce/customer'), WindowsPath('ecommerce/sales2.py'), WindowsPath('ecommerce/shopping'), WindowsPath('ecommerce/__init__.py'), WindowsPath('ecommerce/__pycache__')]
print(paths)

#
# path.iterdir() limitation:
# 1. cannot search by pattern
# 2. doesn't search recursively
#
# use path.glob
# path.glob("*.*") - for all files
#
py_files = [p for p in path.glob("*.py")]
# output:py_files: [WindowsPath('ecommerce/sales2.py'), WindowsPath('ecommerce/__init__.py')]
print('py_files:', py_files)
#
# recursive glob
py_files = [p for p in path.rglob("*.py")]
# output:r_py_files: [WindowsPath('ecommerce/sales2.py'), WindowsPath('ecommerce/__init__.py'),
# WindowsPath('ecommerce/customer/contact.py'), WindowsPath('ecommerce/customer/__init__.py'),
# WindowsPath('ecommerce/shopping/sales3.py'), WindowsPath('ecommerce/shopping/__init__.py')]
print('r_py_files:', py_files)
#
#
### Files ###
# from pathlib import Path
path = Path("ecommerce/__init__.py")
print(path.exists())            # output:True
# output:
# stat: os.stat_result(st_mode=33206, st_ino=3940649674295582,
# st_dev=943563076, st_nlink=1, st_uid=0, st_gid=0, st_size=172,
# st_atime=1587135455, st_mtime=1587135455, st_ctime=1587108668)
#
# st_size: size of file in bytes
# all time values are in seconds after epic which is the start of time on a computer
# and that is plafform dependent. Unix (Posix) and Windows: 1-Jan-1970
# st_atime: last access time
# st_mtime: last modify time
# st_ctime: creation time
print("stat:", path.stat())
#
# from time import ctime
print(ctime(path.stat().st_ctime))      # output:Fri Apr 17 15:31:08 2020


# calculate the epic time
# today minus the seconds values
# from datetime import datetime, timedelta
X = 1587135455
result = datetime.now() - timedelta(seconds=X)
print(result)                           # output:1970-01-01 20:06:07.846287

#
path = Path("file.txt")
path_new = Path("newfile.txt")
# write to file
# use string to write (override the whole file)
path.write_text("New data in string")
#
# use bytes to write (override the whole file)
text_bytes = b"New data in bytes"
print("text_bytes:", type(text_bytes))
path.write_bytes(text_bytes)

# path.write_text("New data in string, again")

# read file into bytes
content_bytes = path.read_bytes()
print(type(content_bytes))              # output:<class 'bytes'>
# output:b'print(__name__, " package is loaded")\r\n'
print(content_bytes)
#
# read file into string
content_str = path.read_text()
print(type(content_str))              # output:<class 'str'>
# output:print(__name__, " package is loaded")
print(content_str)
#

### rename file ###
if path.exists() and not path_new.exists():
    path.rename(path_new)

### delete file - unlink() ###
# output:newfile.txt  file exist: True
print(path_new, ' file exist:', path_new.exists())
path_new.unlink()     # delete file
# output:newfile.txt  file exist: False
print(path_new, ' file exist:', path_new.exists())

#

# path object is easier to use as it handle the file close() befind the scene
# use open(), need to handle file.close() or use with
with open("ecommerce/__init__.py", 'r') as file:
    # output:ecommerce/__init__.py file is opened.
    print("%s file is opened." % file.name)
    content_str = file.read()
    print(type(content_str))              # output:<class 'str'>
    # output:print(__name__, " package is loaded")
    print(content_str)
#
### copy file ###
source = Path(r"ecommerce\__init__.py")
target = Path() / "init.txt"
target.write_text(source.read_text())
# output:init.txt :  print(__name__, " package is loaded")
print(target, ": ", target.read_text())
#
# better way, use shell utility
# import shutil
shutil.copy(source, target)
#
#
### zip files ###
# write to zip file
#
# from zipfile import ZipFile
# w - write mode
# zip = ZipFile("files.zip", "w")
with ZipFile("files.zip", "w") as zip:
    # generator
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
# zip.close()
#
# read from zip file
# read mode by default
# output:
# ['ecommerce/sales2.py', 'ecommerce/__init__.py', 'ecommerce/customer/contact.py',
# 'ecommerce/customer/__init__.py', 'ecommerce/customer/__pycache__/contact.cpython-38.pyc',
# 'ecommerce/customer/__pycache__/__init__.cpython-38.pyc', 'ecommerce/shopping/sales3.py',
# 'ecommerce/shopping/__init__.py', 'ecommerce/shopping/__pycache__/sales3.cpython-38.pyc',
# 'ecommerce/shopping/__pycache__/sales_module3.cpython-38.pyc', 'ecommerce/shopping/__pycache__/__init__.cpython-38.pyc',
# 'ecommerce/__pycache__/sales2.cpython-38.pyc', 'ecommerce/__pycache__/sales_module2.cpython-38.pyc',
# 'ecommerce/__pycache__/__init__.cpython-38.pyc']
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print("size:", info.file_size)                  # output:size: 39
    print("compress_size:", info.compress_size)     # output:compress_size: 39
    # extract to unzip folder
    zip.extractall("unzip")

#
#
### Comma Separated Values (CSV) files ###
# import csv
# have to use open(), cannot use path
# write to CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    # add header for 1st row
    writer.writerow(["transaction_id", "product_id", "price"])
    # add data records
    # Shift+Alt+down arrow  to duplicate the line
    # Ctrl+Shift+K          to delete line
    #
    writer.writerow([1001, 101, 199.99])
    writer.writerow([1002, 102, 299.99])
# issue on Python 3.8.2 on Windows, extra \n for every row
#
# read CSV
# output:[['transaction_id', 'product_id', 'price'], [], ['1001', '101', '199.99'], [], ['1002', '102', '299.99'], []]
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    #
    # can iterate,
    # no output as the index has been pointed to the end by above statement
    # comment out: print(list(reader)) and retry
    # output:
    #     ['transaction_id', 'product_id', 'price']
    # []
    # ['1001', '101', '199.99']
    # []
    # ['1002', '102', '299.99']
    # []
    for row in reader:
        print(row)
#
#
# JavaScript Object Notation (JSON) file
#
# import json
# from pathlib import Path

# list of dictionary
movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Terminator 2", "year": 1991}
]

data = json.dumps(movies)
# output:[{"id": 1, "title": "Terminator", "year": 1984}, {"id": 2, "title": "Terminator 2", "year": 1991}]
print(data)
# write to file
Path("movies.json").write_text(data)
#
# read from file
data = Path("movies.json").read_text()
# convert string to list of dictionary
movies = json.loads(data)
print(type(movies))             # output:<class 'list'>
# output:[{'id': 1, 'title': 'Terminator', 'year': 1984}, {'id': 2, 'title': 'Terminator 2', 'year': 1991}]
print(movies)
print(movies[0]["title"])       # output:Terminator
#
#
### SQLite Database ###
# import sqlite3
# import json
# from pathlib import Path
#
movies = json.loads(Path("movies.json").read_text())
# output:[{'id': 1, 'title': 'Terminator', 'year': 1984}, {'id': 2, 'title': 'Terminator 2', 'year': 1991}]
print(movies)
# output:sqlite3.OperationalError: no such table: Movies
# download the SQLite Browser to create table first
# http://www.sqlitebrowser.org/dl/
#
# or use ddl to create the table
db_file = "movies.sqlite3"
table_name = "Movies"
with sqlite3.connect(db_file) as conn:
    # drop table
    ddl = "drop table if exists " + table_name
    conn.execute(ddl)

    # create table
    ddl = "create table if not exists " + table_name + '''
    (
        id int,
        title text not null,
        year int not null,
        primary key(id)
    )'''
    conn.execute(ddl)

    # insert data
    sql = "insert into " + table_name + " values(?, ?, ?)"
    for movie in movies:
        conn.execute(sql, tuple(movie.values()))
    conn.commit()

    # read data
    sql = "select * from " + table_name
    cursor = conn.execute(sql)
    # cursor is iterable object
    # output:
    # (1, 'Terminator', 1984)
    # (2, 'Terminator 2', 1991)
    for row in cursor:
        print(row)
    #
    # cursor is forward only
    # comment out for loop above to get below result
    # output:[(1, 'Terminator', 1984), (2, 'Terminator 2', 1991)]
    movies = cursor.fetchall()
    print(movies)
#
#
#
### Timestamps ###
# import time         # time stamp
# import datetime
print(time.time())    # seconds from epic, output:1587191573.1247127


def send_emails():
    for i in range(3):
        time.sleep(0.01)  # sleep 0.01 second


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)         # seconds, output:1.0125234127044678

#
#
### date time ###
# import datetime
# dt = datetime.datetime(2020,4,18)
#
# from datetime import datetime
dt1 = datetime(2020, 4, 18)
print(dt1)                       # output:2020-04-18 00:00:00
#
#
print(datetime.now())           # output:2020-04-18 16:55:02.478058
print(datetime.today())         # output:2020-04-18 16:55:02.479060
print(datetime.now().date())    # output:2020-04-18

#
# google search: python 3 strptime
# https://docs.python.org/3/library/datetime.html
# down to bottom:  strftime() and strptime() Format Codes'''']
#
# parse string to datetime
dt3 = datetime.strptime("2020/04/18 13:35:59", "%Y/%m/%d %H:%M:%S")
print(dt3)                       # output:2020-04-18 13:35:59
# import time
dt4 = datetime.fromtimestamp(time.time())
print(dt4)                       # output:2020-04-18 17:09:40.984432
#
# display
print(f"{dt4.year}-{dt4.month}-{dt4.day}")  # output:2020-4-18
#
#
# convert datetime object into string (format string)
#
print(dt4.strftime("%Y-%m-%d %H:%M:%S"))     # output:2020-04-18 17:12:55
#
# compare dates
print(dt4 > dt3)        # output: True
#
#
### Time Delta ###
dt1 = datetime(2020, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
# output:108 days, 17:25:42.374883
print(duration)
#
# output:days 108
print("days", duration.days)
#
# output:seconds 62742
# only for 17:25:42.374883 portion, not including days
print("seconds", duration.seconds)
#
# output:9393942.374883
# include all 108 days, 17:25:42.374883
print("total_seconds", duration.total_seconds())
#
# don't have .months or .years because
# varying amount of time in a month or in a year
#
# timedelta
#
dt1 = datetime(2020, 1, 1) + timedelta(days=1,
                                       hours=11, minutes=22, seconds=33)

print(dt1)      # output:2020-01-02 11:22:33
#
#
#### random ###
# import random
# random number between 0 and 1 (inclusive)
print(random.random())                          # output:0.9087899712551202
# random integer number between 1 to 10 (inclusive)
print(random.randint(1, 10))                    # output:10
# random pick an item from list
print(random.choice([1, 2, 3, 4, 5]))           # output:2
# random pick number of items from list
print(random.choices([1, 2, 3, 4, 5], k=2))     # output:[3, 1]
#
# generate random password

# import secrets
# import string
alphabet = string.ascii_letters + string.digits
#
# for 6-char password
# use random.choices
print(''.join(random.choices(alphabet, k=6)))   # output:CQicBr

# use secrets module
password = ''.join(secrets.choice(alphabet) for i in range(6))
print(password)                                 # output:Ofuyn5
#
# shuffle the list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)                                  # output:[2, 4, 1, 5, 3]
#
#
### opening the browser ###
# import webbrowser
print("Deployment completed")
# webbrowser.open("http://taobao.com")
#
#
### send emails ###
# mime - Multipurpose Internet Mail Extensions
# define the standard of email format (eg. plain text or html)
#
# with MIMEMultipart object, we can send email message that
# include both html and plain text content.
# when the email client of the receiver receives this email message
# if it supports html, it will render the html content; otherwise,
# it will render plain text content.
#
# format:
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
#
# connect to SMTP server
# import smtplib
#
# from string import Template
template = Template(Path("template.html").read_text())
#
# can pass a dictionary that contains key value pairs
body = template.substitute({"name": "Panco"})
# or pass keyword arguments
body = template.substitute(name="Panco")
#
message = MIMEMultipart()
message["from"] = "Panco Cheong"
message["to"] = "panco.cheong@hotmail.com"
message["subject"] = "This email is sent by Python app"
# don't have message["body"], use .attach the payload
# payload can be text, image or other types supported by mime protocol
# message.attach(MIMEText("This is email body in plain text", "plain"))
message.attach(MIMEText(body, "html"))
#
# attach image - in bytes
message.attach(MIMEImage(Path("face.png").read_bytes()))
#
# output:smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials p11sm19702168pff.173 - gsmtp')
# TLS - Transport Layer Security - all commands sent to server are encrypted
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()         # initialize the connection
    smtp.starttls()     # puts smtp connection in TLS mode
    smtp.login("panco.cheong@gmail.com", "yvnnxqkezmtidobe")
#    smtp.send_message(message)
    print("Sent...")
#
#
#
### email template ###
# in real application, email body in separate file, not inside the code
# use HTML to build the template
# different templates for different scenarios,
# eg. sign-up, reset password, place an order etc
# we should name those templates based on this scenario
#
# in here, just simple name it template.html
# VS code snippet: !<Tab> --> generate HTML 5 basic content
#
# from string import Template
# template = Template(Path("template.html").read_text())
#
# can pass a dictionary that contains key value pairs
# or pass keyword arguments
# template.substitute()


#
# https://kinsta.com/knowledgebase/free-smtp-server/
# Outgoing Mail (SMTP) Server: smtp.gmail.com
# Use Authentication: Yes
# Use Secure Connection: Yes (this can be TLS or SSL depending on your mail client)
# Username: GMail account (email@gmail.com)
# Password: GMail password
# Port: 465 or 587
#
# Send Mail as Google SMTP
# step 1: 2-step verification enabled on your primary Gmail account
#           https://www.google.com/landing/2step/
# step 2: generate an App password
#           https://security.google.com/settings/security/apppasswords
#           Select the app and device you want to generate the app password for.
#           select Mail, Windows Computer
# step 3: replace the password with App password
#
#
#
#

### sample email ###
# https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
# import smtplib
# from string import Template
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# MY_ADDRESS = 'my_address@example.comm'
# PASSWORD = 'mypassword'


# def get_contacts(filename):
#     """
#     Return two lists names, emails containing names and email addresses
#     read from a file specified by filename.
#     """

#     names = []
#     emails = []
#     with open(filename, mode='r', encoding='utf-8') as contacts_file:
#         for a_contact in contacts_file:
#             names.append(a_contact.split()[0])
#             emails.append(a_contact.split()[1])
#     return names, emails


# def read_template(filename):
#     """
#     Returns a Template object comprising the contents of the
#     file specified by filename.
#     """

#     with open(filename, 'r', encoding='utf-8') as template_file:
#         template_file_content = template_file.read()
#     return Template(template_file_content)


# def main():
#     names, emails = get_contacts('mycontacts.txt')  # read contacts
#     message_template = read_template('message.txt')

#     # set up the SMTP server
#     s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)

#     # For each contact, send the email:
#     for name, email in zip(names, emails):
#         msg = MIMEMultipart()       # create a message

#         # add in the actual person name to the message template
#         message = message_template.substitute(PERSON_NAME=name.title())

#         # Prints out the message body for our sake
#         print(message)

#         # setup the parameters of the message
#         msg['From'] = MY_ADDRESS
#         msg['To'] = email
#         msg['Subject'] = "This is TEST"

#         # add in the message body
#         msg.attach(MIMEText(message, 'plain'))

#         # send the message via the server set up earlier.
#         s.send_message(msg)
#         del msg

#     # Terminate the SMTP session and close the connection
#     s.quit()


# if __name__ == '__main__':
#     main()

#
#
#
### command line arguments ###
#
# in termial:
# python 07_standard_library.py -a -b -c
#
#import sys
# output:['.\\07_standard_library.py', '-a', '-b', '-c']
print(sys.argv)
#
# output:Usage: python app.py <password>
if len(sys.argv) == 1:
    print("Usage: python app.py <password>")
else:
    # output:Password -a
    password = sys.argv[1]
    print("Password", password)
#
#
### run external program ###
# run "ls" in Linux / MacOS X
# run "dir /ON" in Windows
#
#import sys
#import subprocess
# preferred approach, it create an instance of the Poopen class
# capture_output=True ==> output to stdout
# text=True ==> use string instead of bytes
# check=True ==> raise exception if return is non-zero
#
# completed = subprocess.run(["dir","/ON"], capture_output=True, text=True, check=True)
completed = subprocess.run(r"notepad.exe C:\repos\Python\Programmer\init.txt")
# output:<class 'subprocess.CompletedProcess'>
print(type(completed))
# output:args: notepad.exe C:\repos\Python\Programmer\init.txt
print("args:", completed.args)
print("returnCode:", completed.returncode)  # returnCode: 0
print("stderr:", completed.stderr)          # stderr: None
# , capture_output=True - output save to stdout
print("stdout:", completed.stdout)          # stdout: None
#
#
# run other Python script
print("Run external Python Script")
try:
    completed = subprocess.run(
        ["python", "app.py"], capture_output=True, text=True, check=True)
    # false is only for MacOS X
    # completed = subprocess.run(
    #     ["false"], capture_output=True, text=True)
    # output:args: notepad.exe C:\repos\Python\Programmer\init.txt
    print("args:", completed.args)
    print("returnCode:", completed.returncode)  # returnCode: 0
    print("stderr:", completed.stderr)          # stderr: None
    print("stdout:", completed.stdout)          # stdout: None
    if completed.returncode != 0:
        print(completed.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)

# Process Open
# https://stackabuse.com/pythons-os-and-subprocess-popen-commands/
# subprocess.Popen
#theproc = subprocess.Popen([sys.executable, "myscript.py"])
# theproc.communicate()

# legacy process - not recommended to use below
# subprocess.call
# subprocess.check_call
# subprocess.check_output
