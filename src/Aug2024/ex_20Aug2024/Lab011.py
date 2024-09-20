# Conditions & Loops

'''
Conditions -
'''

# 1. age is >= 18 -> you are allowed to vote - Ture? -> True
# 2. age is < 18 ->  are you allowed to vote ? No -> False
# 3. checks the given condition is true or false
''' If else loop '''

''' Syntax '''

'''
if condition:
    //code you want to execute if the condition is true
else:

    // code you want to execute if the condition is false
'''

# write a program to take user age and let him know if he can go to club

age = int(input("Enter your age: "))
if age >= 20:
    print(f"You are allowed to go to the club with the age {age}")
else:
    print(f"You are not allowed to go to the club with the age {age}, u should be 20 or above")

# Problem to find max between two numbers by taking user input

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
if num1 > num2:
    print("Max is", num1)
else:
    print("Max is", num2)

# if there is more than 1 condition, then use if, elif, else

number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))
number3 = int(input("Enter number3"))

if number1 > number2 and number1 > number3:
    print("The greatest of 3 numbers is: ", number1)
elif number2 > number1 and number2 > number3:
    print("The greatest of 3 numbers is: ", number2)
else:
    print("The greatest of 3 numbers is: ", number3)