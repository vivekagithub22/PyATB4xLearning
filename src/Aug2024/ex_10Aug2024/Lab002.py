#sep=' ' - how you want to separate the arguments
#end='\n' - in the end what you want to do
import keyword

print("Hello", "World", 123, 3.14, True) #here by default the separator is space
print("Hello", "World", 123, 3.14, True, sep="-") # sep acts as a separator between arguments (default is a space). what ever used inside " " will separate the arguments.
print("Hello", "World", 123, 3.14, True, sep="|", end="_") # end specifies what should be printed at the end of the output instead of the default newline character (\n). end="_" ensures that _ is printed instead of a newline after the first print() statement, so the next print() statement continues on the same line.
print("viveka") # sep=" ", end=" " are called parameters that controls how output is formatted.

# Python follows indentation, to define the structure and scope of code blocks
"""
   print("Hello") #identation error, select the files and reformat the code
"""

# Source code - code written by humans, human read-able codes, High level language, we have to follow some rules according to programming language

print("Good", "Viveka", sep="?", end="_")
print("Amit")
