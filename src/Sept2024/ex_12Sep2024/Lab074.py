"""
Package -
** Package is a directory, that contains multiple files.
** a special file in python that defines a package -> __init__.py
"""

# how to import and access files from another package

# from package_name.file_name import function_name
from OpenBrowser.Start import start_a_browser
from OpenBrowser.Stop import stop_a_browser

# we can directly call the function
start_a_browser()
stop_a_browser()

print("-------------------------------------")

# with an example
def testcase():
    start_a_browser()
    print("executing a test case")
    stop_a_browser()

testcase()

