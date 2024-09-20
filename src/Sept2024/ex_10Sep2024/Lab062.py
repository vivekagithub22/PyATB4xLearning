# try, except and finally
# file
import os
try:
    full_path = os.getcwd()
    print("path of current working directory: ", full_path)
    full_path_file  = full_path + "/example.txt"
    print("path of current folder and text file : ",full_path_file)

    file = open(full_path_file,'r') # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    print(file.read())
except Exception as fnfe:
    print("File Not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)