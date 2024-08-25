""" Operators - Operators are used to perform some operations by using operands """
# =, +, -, *, /

age = 35
a = 10 + 10 # operands
b = 5 - 2
c = 2 * 2
d = 4 / 2

""" '=' -> Assignment operator is used to assign the right value """
age2 = 65

""" '-' -> unary operator, works with just one value or operand """
# Unary Plus (+): It doesn't change the value but can make the intention explicit. +5 = 5
# Unary Minus (-): Negates the value, turning positive values into negative and vice versa. -5 = -5
# Logical NOT (not): Inverts boolean values.
# Bitwise NOT (~): Inverts all bits of an integer. In binary, 5 is represented as 00000101. Applying the bitwise NOT operator flips all bits, resulting in 11111010, which is -6 in decimal
how_many_lamborghini_u_have = -1,

""" Arithmatic operator """
# +, -, *, /, %
print(2+2)
print(2-2)
print(2*2)
print(2/2)

# x//y - to find quotient
# x%y - to find reminder
# x**y - to find power

print(5//2) # output is quotient, 5 divided by 2
print(5%2) # output is reminder, 5 divided by 2
print(5**3) # output is power, 5x5x5
# eg
print(13//2) # // is quotient
print(13%2) # % is reminder
print(3**4) # ** is power

# x==y - comparison operator, checks whether the values on both sides are equal
# always returns the output as true or false
print(2==2) # True
print(2==3) # False

""" Not operator - Inverts boolean values, always returns the output as true or false """
is_promod_married = True
print(not is_promod_married) # not gives the opposite value
# ! is a concept in java, in python we use 'not'
# eg
j = True
print(not j) # prints the opposite

""" != not equal to - works with int, always returns the output as true or false """
o = 10
p = 20
result = (o != p) # 10 not equal to 20, so True
print(result)

""" Relational operator >, <, >=, <=
# always returns the output as true or false """
x = 10
y = 20
print(x > y) # 10 > 20 - False
print(x < y) # 10 < 20 - True
n = 10
m = 10
print(n >= m) # 10 >= 10 - True

""" Logical operator - or, and -> follows OR, AND gate rules
# always returns the output as true or false """
f = False
t = True
print(f or t) # 0 or 1 = 1 -> True
print(f and t) # 0 and 1 = 0 -> False















