# User defined - 4 types
# 1. They can't return -> non-return
# 2. They can return something
# 3. They have parameters
# 4. They have don't have parameters / arguments

# 1. They can't return -> No return type
# 4. They have don't have parameters / arguments
def greet():
    print("Hello world")

result = greet()
print(result) # they can't return anything

# No return type by passing argument
def greet_by_name(name):
    print("Hello,", name)

greet_by_name("Viveka")

# No Return type with default argument
def say_hello_default_argument(name="pramod"):
    print("Hello,", name)

say_hello_default_argument() # prints default value
say_hello_default_argument("Tushar") #replaces the default value

# Return type by passing Arguments

def sum_of_two_numbers(num1, num2):
    return num1 + num2
result = sum_of_two_numbers(10, 12)
print(result)

# Return type with default Arguments

def sum_of_two_numbers_with_default_arguments(num1=10, num2=34):
    return num1 + num2
result1 = sum_of_two_numbers_with_default_arguments()
print(result1)














