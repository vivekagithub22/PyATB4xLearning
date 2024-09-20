# try, except and finally
# file

try:
    file = open('testdata.txt','r') # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    print(file.read())
except FileNotFoundError as fnfe:
    print("File Not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)