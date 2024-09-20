# single parameter, with multiple arguments
def make_pizza(*toppings):
    for topin in toppings: # Used to print the values line by line
        print(topin) # we can also use print(*toppings)

pramod = make_pizza("tomato")
dhhir = make_pizza("Olives", "mushroom", "paneer")
vinay = make_pizza("mushroom", "pinapple", "paneer", "sweetcorn")


# Built in *
r = max(1, 2, 3, 4, 5, 6)
print(r)

# multiple parameter, with only one multiple arguments
def make_pizza1(*toppings_1, base): #we can set multiple parameters, but only one parameter can accept * multiple arguments
    print(*toppings_1, base) # instead we can use (base, *toppings_1)

make_pizza1("onion", "mushroom", "cheese", base= "thin crust") # since *argument is in the first position it keeps on accepting values, incase if we want tell it's the value for second position we need to mention base (parameter name)

# same with position change
def make_pizza2(base1, *toppings_2): #we can set multiple parameters, but only one can accept * multiple arguments
    print(base1, *toppings_2)

make_pizza2("double crust", "tomato", "sausage", "onion", "cheese") # since *argument is in the second position, we no need to specify the parameter name. after accepting single argument to the first parameter, system starts assigning remaining arguments to the *parameter by default






