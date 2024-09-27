# Literals
# Variable name(identifiers) = Variable value (Literals)
# Literals determine the data type
age = 35 #int literals, data type of age is int
viveka_married = False #Boolean literals, data type of variable is boolean
pi = 3.14 #Float literals
name = "Viveka" #Sting literals
short_name = 'v' #Character literals

# on rare cases we may use binary, octal, hexa

# Character literals -
# Single character enclosed in single quotation marks
# Escape Sequence
# ASCII Value
# UNICODE Character
# Octal Character

# Escape sequence -
print("Hello World")
print("Hello\nWorld") # \n newline
print("Hello\tWorld") # \t tab
print("Hello\bWorld") # \b backspace

# r -> raw string
# directory_name = 'c:\pramod\n.txt' # \n will convert the path to newline
# directory_name = "c:\pramod\n.txt" # \n will convert the statement to newline
directory_name = r"c:\pramod\n.txt"# r -> raw string will stop the conversion from newline or tab (escape sequence)
directory_name2 = r'c:\pramod\n.txt'
print(directory_name)
print(directory_name2)
# r concept will be used in API and Web automation, where ever we use the file path
# r works with both single and double quotes

# single quote escape sequence
#name = 'Viveka's' # error occurs when single quote is used inside single quotes, so use \ before '
name = 'Viveka\'s'
name2 = "Viveka's" # single quotes can be used within double quotes


