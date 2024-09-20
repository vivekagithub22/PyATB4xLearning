"""
Task #3
- Explain the difference between the = operator and the == operator in Python.

- What does the ** operator do in Python, and how is it used?

- What does the ^ operator do in Python, and in what context is it commonly used?
"""

# '=' operator - assignment operator is used to assign values to a variable,

# '==' operator - is used for comparison, It checks whether the values on both sides are equal. which returns a Boolean result (True or False).

# '**' operator -
# '**' operator is used for exponentiation
# is used to raise a number to a power.
# For example, base ** exponent means you take the base number and raise it to the power of the exponent.
# base ** exponent

# ^ operator -
# The ^ operator is the bitwise XOR (exclusive OR) operator.
# The ^ operator compares each bit of two integers. For each bit position:
# The result bit is 1 if the corresponding bits of the operands are different
# (one is 1 and the other is 0).
# The result bit is 0 if the corresponding bits are the same (both 0 or both 1).
a = 12   # binary: 1100
b = 7    # binary: 0111
result = a ^ b  # binary: 1011 x Powers:  2^3 2^2 2^1 2^0, add the result
print(result)   # Output: 11

c = 14 # binary 1110
d = 9  # binary 1001
output = c ^ d # binary: 0111
print (output)

# The ^ operator is commonly used in contexts like: Cryptography: For encrypting and decrypting data using XOR operations
# Bit manipulation: For performing operations on individual bits of a number Checking for unique elements in a list or set

"""
Task #4
Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
"""
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print(f"Area of a circle with radius {radius} is {area:.4f} square units")

"""
Task #5
- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
"""
# Ternary operator
num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

"""
Task #6
- Develop a Python script that calculates the square and cube of a given number.
"""
number = int(input("Enter the number: "))
square = number ** 2
Cube = number ** 3
print(f"The square of {number} is {square}")
print(f"The cube of {number} is {Cube}")

