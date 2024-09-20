# Create a program to sum three number by taking user input

def sum_of_three_num(num1, num2, num3):
    return num1 + num2 + num3
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
result = sum_of_three_num(num1, num2, num3)
print("Sum of three numbers is: ", result)

# sum of two numbers, by passing arguments. without user input

def sum_of_two_numbers(a, b):
    return a + b
result1 = sum_of_two_numbers(10, 20)
result2 = sum_of_two_numbers(20, 30)
print(result1)
print(result2)

# sum of 3 numbers by giving one default argument, remaining values passed as arguments

def sum_of_3_with_one_default_value(x, y, z=15):  #(x=2, y, z) or (x, y=2, z) -> parameter without default value cannot follow parameter with default value, we can assign default value to the last parameter, otherwise we should assign default value to all the parameters, else we should not assign default value to any of the parameters
    return x + y + z
result3 = sum_of_3_with_one_default_value(10, 20)
print(result3)

# sum of numbers by giving default arguments

def sum_of_numbers_with_default_arguments(m=5, n=10, o=15):
    return m + n + o
result4 = sum_of_numbers_with_default_arguments()
result5 = sum_of_numbers_with_default_arguments(10, 20, 30)
print(result4)
print(result5)