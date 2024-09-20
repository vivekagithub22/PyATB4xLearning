""" *args = Multiple arguments with no limit -> similar to list"""
# No return type with argument function -

def print_arguments(*args):
    print(args[0]) # args[0] specifies - argument from the place of index number 0 will be printed
    # if we want to print all the arguments use below
    # for i in args:
    #      print(i)
# eg: list = ["promod", "amit", "lucky"]
print_arguments("pramod", "amit", "lucky") # these arguments are similar to list
print_arguments("amit", "lucky")
print_arguments(10, "pramod", True)
print_arguments("pramod", "amit", 12, True, False, 3.14)
print_arguments(34.56, 56, "viveka")
# *args = minimum 1 argument is necessary

# print() accepts multiple arguments
print("Viveka")
print("Vive", "varthini", 10, True, False, 3.14)
print(22, 3.14, 55.8)

# When we are working with the functions, and want to pass multiple arguments we need to use * before the parameter