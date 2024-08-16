# Aug 10, 2024
#sep=' ' - how you want to separate the arguments
#end='\n' - in the end what you want to do
import keyword

print("Hello", "World", 123, 3.14, True) #here by default the separator is space
print("Hello", "World", 123, 3.14, True, sep="-") # here '-' will act as the separator between each word. what ever used inside " " will separate the words.
print("Hello", "World", 123, 3.14, True, sep="|", end="_") # As we know the code in the next line prints the output in the next line. end= " " is used to bring the next line output to the same line. what ever used inside " " will connect the two lines
print("viveka")

# Python follows indentation, there should not be space left at the beginning of each source code
"""
   print("Hello") #identation error, select the files and reformat the code
"""

# Source code - code written by humans, human read-able codes, High level language, we have to follow some rules according to programming language

print("Good", "Viveka", sep="?", end="_")
print("Amit")

# Keywords & Identifiers - called as reserved words
# can be in lower case or upper case
# cannot be used as variable name or function name
# Keywords are case-sensitive

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Variable name - used to store the values, like containers
age = 25 # variable name = variable value, variable is also called as identifier
print(age)
age = 30
print(age) # advantage of variable is we can change the value, though it already holds a value. The old value will be over-ridden with the new value.

# Create a variable
# 1. Type of the container is Data type. (data type is the type of the value stored)
# 2. Name of the container - variable name
# 3. Value stored in the container - variable value

# Different type of data type in Python
# 1. Numeric data type
# a. Integer (whole numbers: -8748374,-1,0,1,9987,98787766)
# b. Float - 3.14, 18.45, 3.128487857
# c. complex - iota(1+2j), root number - we don't use complex in automation
# d. boolean - True or False

# 2. String data type
# a. bunch of character -> viveka
# b. single character

# 3. List - [], we don't have array in python
# a. shopping_list = ["milk", "bread", "jam"]
# b. mark_list = [10,20,30]
# c. mixed_list = ["alpha", 133]

# 4. Advanced data type
# a. set, dictionary, tuple, binary, frozen set

# Rule of variable name
# 1. Can start with letters (A-Z or a-z), bunch of letters, and can be followed by numbers
# 2. Can be under-score (_), can be followed by 0, digits (0-9), or more letters
# 3. Python is case-sensitive, myVariable & myvariable are two different identifiers
