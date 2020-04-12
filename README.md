# bike_backend

## About the Stack
---
**Django:** a Web framework written in Python. Easy for developers to quickly build prototypes. Lots of built-in APIs and sub-frameworks like DegoDjango.

**GeoDjango:** a built-in application that is included as a contrib module in Django. To use GeoDjango, you need a spatial database and geospatial libraries.

**Virtual Enviornment:** Like a sandbox for each Django project. External libraries that support development will be in an isolated enviornment so dependencies won't clash


## Getting Started
---

To activate your virtual enviornment: source env/bin/activate

To fully use all features of GeoDjango, install the following open-source geospatial libraries:
1. GEOS (Geometry Engine Open Source) - C++ port of the Java Topology Suite that implements the OCG Simple Feature for SQL Specification
2. GDAL (Deospatial Data Abstraction Library) - an open-source library for working with raster and vector geospatial data formats
3. PROJ.4 (Cartographic Projects library) - an open-source GIS library for easily working with spatial reference systems and projections
4. GeoIP - A library that helps users find geographical information based on an IP address.

$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip

Add to your .bash_profile. 

export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/X.Y/bin
    Where X.Y is your current PostgreSQL version

export PATH=/Library/Frameworks/UnixImageIO.framework/Programs:$PATH
export PATH=/Library/Frameworks/PROJ.framework/Programs:$PATH
export PATH=/Library/Frameworks/GEOS.framework/Programs:$PATH
export PATH=/Library/Frameworks/SQLite3.framework/Programs:$PATH
export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH
export PATH=/usr/local/pgsql/bin:$PATH

Thanks to Djangos Object Relational Mapping feature (ORM), we dont need SQL to create the databases. Just use python's migrate f=

$ python manage.py makemigrations
$ python manage.py migrate

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
3. brew install gdal