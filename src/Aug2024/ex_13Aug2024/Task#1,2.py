# Homework 13th Aug -
# Task 1 - To create a program by taking user input and print a table
# 1. f"{} sting format concept
# 2. User input -> number 10,100,2,-1,3.14
# 3. 9*1=9
# 4. till 10

table = int(input("Enter which table would you like to print")) #mention float to give input in decimal
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")

# Task 2 - To create a program, take 2 user inputs as num1 & num2 and give them
# 1. Max, min, sum, sub, mul, div
# 2. pow num1 to num2
# 3. format out with f"{}"

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
print("Maximum of two numbers is:", f"{max(num1,num2)}")
print("Minimum of two numbers is:",f"{min(num1,num2)}")
print("Sum of two numbers is:",f"{(num1+num2)}")
print("Subtraction of two numbers is:",f"{(num1-num2)}")
print("Multiplication of two numbers is:",f"{(num1*num2)}")
print("Division of two numbers is:",f"{(num1/num2):.4f}")
print("Power of two numbers is:", pow(num1,num2))



