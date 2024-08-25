# Write a program to calculate area of a circle
# area = π * r^2 (take pi as 3.14)

# Logic building formula
# Step 1
# Figure out the input and output
# get output for r
# pi = 3.14 or math.pi
# power -> pow or **

# o/p -> float -> print area

# Step 2
# rough logic -> area = 3.14 * pow(r,2)

# Step 3 - write the code
# My code
"""
radius = float(input("Enter the radius"))
area = 3.14 * pow(radius,2)
print(area)
"""
import math

# Promod code
radius = float(input("Enter the radius"))
print(radius)
print(math.pi)
area = math.pi * pow(radius,2)
print("Area of a circle is", area)
print("Area of a circle is", f"{area:.3f}")

# one line code
"""
print(f"Area of a circle is, {3.14 * pow((float(input("Enter the radius"))), 2):.3f}") # with pow()
print(f"Area of a circle is, {3.14 * (float(input("Enter the radius")) ** 2):.3f}") # with **

"""
