""" Tuple """

# 1. Tuple is a collection of items, allows duplicates
my_tuple = (1, 4, 6, 8, 8)
# 2. They are immutable in nature, values cannot be replaced or reassigned
# my_tuple[0] = 3 -> tuple doesn't support item assignment
# 3. Less memory usage, due to fixed list of elements
# 4. Tuple uses () parenthesis
# 5. Fixed data

# 6. If we want a fixed list of elements, then we have to use tuple
my_fixed_accounts = ("testacademy.com", "sdet.club")

# Converting tuple to list is also possible
my_tuple_list = ("testacademy.com", "sdet.club")
my_conversion_to_list = list(my_tuple_list) #conversion
print(my_conversion_to_list)
# again we can convert it to tuple by using 'tuple'
my_conversion_to_tuple = tuple(my_conversion_to_list)
print(my_conversion_to_tuple)

# simplified example
t1 = list(("viveka", 5016)) # conversion of tuple to list
print(t1)
t2 = tuple(["Vivekavarthini", "K"]) # conversion of list to tuple
print(t2)


# Real case, where we use tuples, fixed urls -> we knew it's not going to change so use tuples
API_URLs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestacademy.com")
print(API_URLs[0])
print(API_URLs[1])

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("wonder woman", "diana prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[1][1])

# we can also assign this way
a, b , c = (10, 11, 12)
print(a)
print(b)
print(c)

# search using tuple
cities = ("London", "Paris", "Tokyo")
print("Paris" in cities) # -> True - gives output in boolean
print("New delhi" in cities) # -> False - gives output in boolean

# we cannot use append with tuple directly
t = (12, 34, 56)
# t.append(12) # throws error
print(t)
# convert tuple into list first and then append
convert_tuple_to_list = list(t)
convert_tuple_to_list.append(12)
# convert it back to tuple
t = tuple(convert_tuple_to_list)
print(t)



