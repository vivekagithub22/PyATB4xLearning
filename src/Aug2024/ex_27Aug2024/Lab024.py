
"""Real time example"""
import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Start time= ",start_time)
        func()
        end_time = time.time()
        print("end time= ",end_time)
        print(f"time taken by function is {end_time - start_time}")
    return wrapper()

@time_decorator
def test_ui():
    print("Add a function, time taken by this function")
    time.sleep(2)

@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(5)


# Multiple decorators

def decorator1(func1):
    def wrapper1():
        print("Decorator1")
        func1()
    return wrapper1

def decorator2(func1):
    def wrapper1():
        print("Decorator2")
        func1()
    return wrapper1

@decorator1
@decorator2
def say_hello():
    print("Hello")

say_hello()

