print(" --- Start of the program --- ")
try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int()
    b = int(input("Ent the num2")) # Lab150.py", line 4, ValueError
    c = a / b # ZeroDivisionError: division by zero - Lab149.py", line 3
    print("Result Div is ", c)
except Exception as e: # alias , Exception is what Class - multiple classes
    print(e)
    print("Please check your inputs, it should not be a string or b value should not be zero")


print(" --- End of the program ---")

# Concept -
# try :
#     # Try this code
# except:
#     # Execute me if try has some error