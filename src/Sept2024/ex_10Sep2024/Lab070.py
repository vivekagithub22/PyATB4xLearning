# how to read lines

with open('afile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)


"""
file = open('afile.txt')
content = file.read()
print(content)
"""