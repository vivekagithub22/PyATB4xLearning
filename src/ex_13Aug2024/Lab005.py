# take input from user and print Hi, your name
""" The input() function is used to get user input from the console."""
name = input("Enter your name")
print("Hi,",name)
print(type(name))

# for example, get user input in alphabets and check the data type
# for example, get user input in numbers and check the data type, though the value you provide in numbers the data type displays as string because input function always considers the user input as string


# take a user input num1 & num2 and calculate sum, sub, mult, div
""""
num1 = input("Enter the num1")
num2 = input("Enter the num2")
print("sum is:", num1+num2) # since the 'input' function takes data as string, the values that user input will get concatenated as 8989, instead of 89+89 = 178
print("sub is:", num1-num2) # hence remaining code gives error due to the data type string
print("mul is:", num1*num2)
print("div is:", num1/num2)
"""
# In Python, the input() function always returns data as a string, regardless of what the user types. If you want to work with numbers, you need to convert that string into a numeric type. That's where we use int()

num1 = int(input("Enter the num1")) # thus we have to first convert the user input to int
num2 = int(input("Enter the num2"))
print("sum is:", num1+num2)
print("sub is:", num1-num2)
print("mul is:", num1*num2)
print("div is:", num1/num2) # while JAVA eliminates the decimal values and displays only integer in case of division,
# Python is a ver smart lang as it displays the result of division in float since there is a high chances for decimal value in division

# if we want to see two or more digits after decimal then we have to use String formating f"{}"

number = 3.14159265359
formated_number = f"{number:.4f}"
print(formated_number)

# write a table

table = 9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
# value inside {} will be executed and value outside {} are string

