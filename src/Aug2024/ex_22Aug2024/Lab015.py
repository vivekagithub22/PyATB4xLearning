""" Match Statement """
# Switch in Java
# Match the output and execute

# match variable:
#     case pattern1:
#          # code block
#     case pattern2:
#          # code block

# Write a program to ask the user which browser he wants to run
browser_name = input("Enter the browser name")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("browser not found")


# another example
user_type = input("Enter the user type: admin, manager or guest")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello Guest")
    case _:
        print("Hello There!")