"""
Task #7
✅ Leap Year Checker:
https://github.com/PramodDutta/PyATB4xLearning/blob/main/src/tasks/img_1.png?raw=true

Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
"""

# condition is -
# year divisible by 4, so it's a leap year
# Year 2024 divisible by 4 and not divisible by 100, so it's a leap year
# Year 1900 divisible by 4, 100 and not divisible by 400, so it's not a leap year
# Year 2000 divisible by 4, 100, 400, so it's a leap year

"""
Condition -

The year 2000 is a leap year because it is divisible by 400.
The year 1900 is not a leap year because, although it is divisible by 100, it is not divisible by 400.
The year 2024 is a leap year because it is divisible by 4 and not divisible by 100.
"""

Year = int(input("Enter the year to check whether it is a leap year or not: "))
if (Year%4 == 0 and Year%100 != 0) or Year%400 == 0:
    print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")