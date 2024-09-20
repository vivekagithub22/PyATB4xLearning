"""
An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

- Any event which disrupt the normal flow of a program when an error occurs.
- They can arise from various situations, such as invalid operations or unexpected conditions.
- Understanding **how to handle exceptions** is crucial for writing robust Python code.

Errors and exceptions in Python are both mechanisms that indicate problems in a program.

**Error**

These are typically caused by mistakes in the code, such as syntax errors or logical flaws.

For example, a `SyntaxError`

**Exceptions**

These are runtime issues that occur during the execution of a program.

- trying to divide by zero or accessing an invalid index in a list.
- For example, a `TypeError` occurs when an operation is performed on incompatible data types.

"""

#print(x) # NameError: name 'x' is not define
#print(10/0) # ZeroDivisionError: division by zero
#print(1+"1") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(int('a')) # ValueError: invalid literal for int() with base 10: 'a' | valid : print(int(3.12))
#my_list = [1, 2, 3]
#print(my_list[5]) # IndexError: list index out of range
#while True print("Hello World") # SyntaxError: invalid syntax
     #print("hello World")  # IndentationError: unexpected indent

