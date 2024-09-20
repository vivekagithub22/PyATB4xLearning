
# Function scope
global_v = 12 # as per the indentation, the variable is directly accessible within the functions as well as outside the function
def fun():
    a = 10 # local variable, is accessible only within the same function
    print(a)
    print(global_v)

def fun1():
    print(global_v) # public variable or global variable is accessible within any function or outside  the function

fun()
fun1()
print(global_v)

"eg:"

public_toilet = "open for all" # outside the function, so open for all

def home():
    private_toilet = "only for home" # private, only inside the particular function. cannot access outside the function
    print(private_toilet)
    print(public_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet) # cannot invoke another function's variable inside any other function
    home() # we can call another function inside any function

print(public_toilet)
stranger()


# inner function
def outer_function():
    variable_1 = 15 # local variable can be accessible within the inner functions

    def inner_function_1():
        print(variable_1)

    def inner_function_2():
        print(variable_1)
    inner_function_1()
    inner_function_2()

outer_function()

