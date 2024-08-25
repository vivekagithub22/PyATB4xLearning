"""
Task #8

✅ Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.

Give three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

"""
# a =  float(input("Enter the length of a: "))
# b =  float(input("Enter the length of b: "))
# c =  float(input("Enter the length of c: "))

a, b, c = map(float,input("Enter all three sides of a triangle, separate them using space: ").split()) # split() format
print(f"Sides of the triangle are: a={a}, b={b}, c={c}")
if a == b == c:
    print("It's an equilateral triangle")
elif a==b or b==c or a==c:
    print("It's an isosceles triangle")
else:
    print("It's a scalene triangle")