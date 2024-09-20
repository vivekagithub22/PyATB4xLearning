# os - Operating system
# os name -> posix - windows or linux, nt - windows
import os

print(os.name)
if os.name == 'posix':
    print("max or linux")

else:
    print("windows")


# print(os.getcwd())
# os.chdir("/Users/promode/Downloads/postman_collections/project1")
# print(os.getcwd())
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#     print(file)


# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')

# full_path = os.path.join('folder path', 'file name.txt') -> this is often used
full_path = os.path.join(r'C:\Users\kuppu\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10Sep2024', 'file.txt')
# "/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/file.text"


print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))

print(os.path.isdir('directory_name'))