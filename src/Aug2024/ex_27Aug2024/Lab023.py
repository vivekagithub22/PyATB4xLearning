""" Decorators """

# Decorators in python are a way to modify the behaviour of a function or class without changing it's source code.
# They are a powerful tool that allows you to wrap another function and extend it's functionality, while keeping the original function's code unchanged

""" Benefits of decorators are: """
# 1. Code Reusability: Decorators promote the DRY (Don't Repeat Yourself) principle by allowing you to reuse code that can be applied to multiple functions. For example, if you need to log function calls, you can write a decorator for logging and apply it to any function that requires logging.

# 2. Separation of Concerns: They help in separating concerns by allowing you to keep the core logic of your function separate from cross-cutting concerns like logging, timing, or access control. This makes your code cleaner and easier to maintain.

# 3. Code Readability: Decorators can make your code more readable by abstracting complex functionality into easily understandable components. Instead of cluttering a function with additional code for authentication or validation, you can apply a decorator that handles this aspect.

""" Primary use of decorators """
# 1. Before
# 2. After
# 3. Logging - add logs to the automation


def add_extra_security(func):  # (func) custom function where you want extra functionality
    #two parts
    #wrapper & call
    def wrapper():
        print("1. Before the function is called")
        print("2. Add helmet, dashcash, gloves, knee guards")
        func() # to call drive_bike() function
        print("3.After the function is called")
        print("4. Secure Driving")
    return wrapper() # it's calling the same function by itself

@add_extra_security  #decorator
def drive_bike():
    print("I am driving")


""" Example """

def before_and_after_ui(func1):
    def wrapper1():
        print("Before running the UI TC")
        print("Start the browser")
        func1()
        print("After running the UI TC")
        print("Quit the browser")
    return wrapper1()

@before_and_after_ui
def test():
    print("Test the UI")

