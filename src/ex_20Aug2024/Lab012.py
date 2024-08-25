"""
Grade calculator:
Write a program that calculate and display the letter grade for given numerical score

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

"""

Marks = int(input("Enter the mark that you scored"))
if Marks >= 90 and Marks <= 100: # simplified format if 90 <= Marks <= 100:
    print("Your Grade is A")
elif Marks >= 80 and Marks <= 89:
    print("Your Grade is B")
elif Marks >= 70 and Marks <= 79:
    print("Your Grade is C")
elif Marks >= 60 and Marks <= 69:
    print("Your Grade is D")
elif Marks >= 0 and Marks <= 59:
    print("Your Grade is F")
else:
    print("Incorrect value")