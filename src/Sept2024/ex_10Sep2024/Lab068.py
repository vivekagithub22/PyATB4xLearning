"""
**File Handling**

1. How to Read a Text, and Write into it using python Code.
2. How to open a file -> file = open("file_name","mode")`
3. `mode ` - `'r' for reading (default).` w' for writing (creates a new file or truncates an existing one).
4. `'a' for appending.`
5. `'b' for binary mode.  zoom.exe - binary`
6. `'+' for updating (reading and writing).`
"""
# Read file

import os
# read a file which is in different folder
full_path = os.path.join(r"C:\Users\kuppu\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10Sep2024\test", "viveka.txt")

file = open(full_path, 'r')
content = file.read()
print(content)

# if we want to access the file inside the same directory, then use file = open('file_name', 'mode'). No need to use os.path.join

# always try to use try except for file handling
try:
    full_path = os.path.join(r"C:\Users\kuppu\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10Sep2024\test",
                             "viveka.txt")

    file = open(full_path, 'r')
    content = file.read()
    print(content)

except FileNotFoundError as fnfe:
    print("FileNotFoundError, fix the path or create a file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)


