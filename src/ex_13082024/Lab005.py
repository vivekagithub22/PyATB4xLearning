# take input from user and print Hi, your name
name = input("Enter your name")
print("Hi,",name)
print(type(name))

# for example, enter the value in alphabets and check the data type
# for example, enter the value in numbers and check the data type, though the value you provide in numbers the data type displays as string because the data type of input function is always string

#take a user input num1 & num2 and calculate sum, sub, mult, div
""""
num1 = input("Enter the num1")
num2 = input("Enter the num2")
print("sum is:", num1+num2) # since the data type of function 'input' is string, the values that we input will get concatenated as 8989, instead of 89+89 = 178
print("sub is:", num1-num2) # hence remaining code gives error due to the data type string
print("mul is:", num1*num2)
print("div is:", num1/num2)
"""

num1 = int(input("Enter the num1")) # thus we have to first convert the user input to int
num2 = int(input("Enter the num2"))
print("sum is:", num1+num2)
print("sub is:", num1-num2)
print("mul is:", num1*num2)
print("div is:", num1/num2) # whereas JAVA eliminates the decimal values and displays integer while division,
# Python is a ver smart lang as it displays the result of division in float since there is a high chances for decimal value

# if we want to see two or more digits after decimal then we have to use String formating

number = 3.14159265359
formated_number = f"{number:.4f}"
print(formated_number)

# write a table

table = 9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
# value inside {} is value and value outside {} is string

