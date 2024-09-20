""" Lambda """

# Lambda is an anonymous function that returns some form of data
# Syntax - Lambda parameter:expression

# for example
"""
def number(num):
    return num * 3
o = number(10) # The result of the function call (which is 30) is assigned to the variable o
print(o) # output is 30
"""

# To simplify the above we use lambda

o = lambda num: num * 3
print(o(10)) # here o acts as a function

# another example
"""
def add_10(n):
    return n + 10

oo = add_10(100)
print(oo)
"""

oo = lambda n: n+10
print(oo(100))

# Problem statement
"""
def sum_three_num(a,b,c)
return a+b+c
"""

q = lambda a,b,c : a+b+c
print(q(1,2,3))


# find_odd_even, lambda simplification
"""
def odd_even(number):
    if number % 2 ==0:
        print("Even")
    else:
        print("Odd")
odd_even(11)
"""
# simplify
check_odd_even = lambda number: "Even" if number%2 == 0 else "Odd"
print(check_odd_even(11))

