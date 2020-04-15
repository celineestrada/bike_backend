# bike_backend

## About the Stack
---
**Django:** a Web framework written in Python. Easy for developers to quickly build prototypes. Lots of built-in APIs and sub-frameworks like DegoDjango.

**GeoDjango:** a built-in application that is included as a contrib module in Django. To use GeoDjango, you need a spatial database and geospatial libraries.

**Virtual Enviornment:** Like a sandbox for each Django project. External libraries that support development will be in an isolated enviornment so dependencies won't clash


## Getting Started
---

To view our web application code, we suggest downloading the Python IDE Pycharm: https://www.jetbrains.com/pycharm/download/#section=mac

For this project, we used Python 3 and the Python Package Installer(PIP). 

For Macs (preferable):
Homebrew: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
Install Python: brew install python3
Usually python3 comes pre-installed with pip, but if you get an error, run: sudo easy_install pip

Virtual Environment: sudo pip3 install virtualenv 
Setup your virtual environment:
cd into the bike_backend folder
virtualenv venv
Activate your virtual environment: source venv/bin/activate
(To deactivate your virtual environment): deactivate

Required Python Modules:
django : python -m pip install django or pip install django
mysqlclient: python -m pip install mysqlclient or pip install mysqlclient
django-crispy-forms: python -m pip install django-crispy-forms or pip install django-crispy-forms 
gdal: brew install gdal (optional)

For Linux (in this order):
Check if python is installed: python3 --version. If not, install latest version with sudo apt-get install python3.8
pip3: sudo-apt install python3-pip
Virtual Environment: sudo pip3 install virtualenv 
Setup your virtual environment:
Cd into the bike_backend folder
virtualenv venv
Activate your virtual environment: source venv/bin/activate
(To deactivate your virtual environment): deactivate

Required Python Modules:
django: pip3 install django
mysqlclient: sudo apt install default-libmysqlclient-dev and pip3 install mysqlclient
django-crispy-forms: pip3 install django-crispy-forms

Setup Database:
Download MySQLWorkbench: https://www.mysql.com/downloads/
In the workbench, create a new connection with the default settings. Make note of the password you’ve created for this database though.
Open the connection and import the schema dump.
In root/settings.py, find the database object (around line 81) and change the set password to the password you picked for your mysql connection. Ensure that the other fields correctly match up with your connection as well.

Run the program:
In your PyCharm terminal after changing directories to the bike folder: python manage.py runserver
The server will be running on http://127.0.0.1:8000/


## Definitions
---
**bash_profile:**  executed to configure your shell before the initial command prompt.

**Web Framework:** a software that supports development of dynamic websites, applications, and services

**Spatial Database:** a database optimized for storing and query data that represents object defined in a geometric space. 

## Helpful links
---
Django 1.8 Setup: https://realpython.com/django-setup/#django-18
Fixing $PATH of mysql/bin: https://stackoverflow.com/questions/10577374/mysql-command-not-found-in-os-x-10-7
Install MySQL and MySQLClient (use pip3 though which is already installed with the most up-to-date version of python 3.8.1): https://ruddra.com/posts/install-mysqlclient-macos/
Half of the fix for Error-1: https://stackoverflow.com/questions/12218229/my-config-h-file-not-found-when-install-mysql-python-on-osx-10-8
This kinda helped for Error-1: https://stackoverflow.com/questions/33717861/error-loading-mysqldb-module-with-django-on-os-x and https://stackoverflow.com/questions/25459386/mac-os-x-environmenterror-mysql-config-not-found
Edit your .bash_profile: https://natelandau.com/my-mac-osx-bash_profile/
https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html

## Git
Check the status: git status
Create a new branch: git checkout -b <name_of_branch>
Stage (aka add/flag for a commit) all changes you have made: git add .
Stage (aka add/flag for a commit) one change you have made: git add <file_name>
Make a commit: git commit -m "<message>"
Push your commits: git push

## Errors Found
---
1. “my_config.h” file not found when installed mysql-python on osx 10.8

## Set Up
1. brew install python3 (this is to get pip3)
2. python -m pip install mysqlclient
3. python -m pip install django-crispy-forms
5. brew install gdal