""" Loops """

""" 1. For loop
# Print hello 10 times
# When we want to repeat the code and print something we use for loop

Syntax:
for 'variable name' in the range(start, stop, step):
    //code that has to be executed multiple times
"""
# for, range ?
# for - keyword, range - in-built function
# giving start, step value is optional

for i in range(1,10): # by default the step value is 1
    print(i)

# it generates a sequence of numbers starting from the start value, ending before the stop value, and incrementing by the step value each time.
# print odd numbers
for j in range(1,10,2): # generates output, incrementing by the step value each time
    print(j)

# print even numbers
for k in range(2,20,2):
    print(k,end=",") # if u want to print the output in the same line using comma

# print hello world 10 times -
for l in range(1,11):
    print("Hello world!", l)

# Interview question :
for number in range(10, 0, -2): # if we want to print the output in reverse, the step value should be given with -
    print(number)


""" Break """
for z in range(1,9):
    print(z)
    if z == 5:
        break

""" For loop with if-else """
for a in range(1, 10):
    if a == 6:
        print(a)
    else:
        print("No O/P")

""" Pass """
for b in range(1, 10):
    if b == 6 or b == 5:
        print(b)
    else:
        pass # prints nothing, until the condition satisfies

""" program to print even numbers """
for c in range(0, 101):
    if c % 2 == 0:
        print(c)
    else:
        pass


""" Continue statement """

# Prints odd numbers
for number in range(10): # if we don't mention start value, by default it takes 0
    if number % 2 == 0:
        continue
    else:
        print(number)