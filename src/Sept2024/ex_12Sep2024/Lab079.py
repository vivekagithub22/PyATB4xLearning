"""
Libraries -
* Is a collection of packages
* Libraries contains multiple packages -> package contains multiple modules -> module is a single file which is file.py
Eg of libraries:
* Pandas library - is used to read csv file and create tables
* Matplotlib - is used to create graphs
* request lib - is used in API automation

## Pandas is a library, that contains multiple packages
-> csv is a package that contains multiple modules, that modules reads csv file
-> ai package
-> ml package
-> computer vision package
"""

# We are interested in

# requests
# webdriver (selenium 4)
# csv , os - modules
# pytest, json, allure report, xml, playwright, openpyxml, openpycsv,

## pip
# pip install library
# pip is a package manager - where you can import the other packages into your own projects.
# Pip is the package installer for Python.
# It allows you to **install and manage additional packages** that are not part of the Python standard library.
# To check for commands in terminal -> pip --help
"""
- **Installing Packages with pip**
    - pip install package_name
    - pip install selenium
    - pip install pytest
    - pip install allure-pytest
    - pip install pandas
- **Upgrading and Uninstalling Packages**
    - pip uninstall package_name
- List download all 
    - pip list -> to see the list of packages installed in the project
- **Managing Dependencies**
    - Pip allows you to specify dependencies in a `requirements.txt`  file.
    - To freeze the requirement - `pip freeze > requirements.txt` # saves all the package into a text file
    - to use the or install the all packages in one way into another a new project - Copy & Paste the requirement file & command -> pip install -r `requirements.txt` 
"""
# Automation Project
# selenium, request, csv, os, pytest, json, playwright
# pip install

import csv

# builtins