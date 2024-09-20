""" Sets """
# 1. Collection of Unique elements
# 2. Set automatically removes duplicate elements
# 3. {} -> uses curly braces

#
list_of_unique_elements = {1, 2, 3, 4, 4, 5, 5, 6} # provides unique output
print(list_of_unique_elements)

# how to remove duplicates from a list
my_list = [43.3, 33, 33, 56, 7] # The order of elements in the output may not match the order in the original list, as sets are unordered collections.
#-> convert list into set
convert_to_set = set(my_list)
print(convert_to_set)
#print(set(my_list))

# How to remove duplicates from a tuple
t = ("Thetestacademy", "for", "Thetestacademy")
print(set(t))

# Union of both the set
set1 ={1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

# Intersection between both the sets
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
my_set1 = set3.intersection(set4)
print(my_set1)

# difference between both the sets
my_set1 = set3.difference(set4)
print(my_set1) # O/p: 1, 2, 3

my_set1 = set4.difference(set3)
print(my_set1) # O/p: 6, 7, 8

# checks all the elements in both sets matches, if yes returns True, if not returns False
set5 = {1,2,3,4}
set6 = {1,2,7}
my_set2 = set6.issubset(set5)
print(my_set2)

# length of set
set7 = {"Thetestacademy", "for", "Thetestacademy."}
print(len(set7))

# print the values of set line by line
for i in set7:
    print(i)

# add element to the existing set
set7.add("Pramod")
set7.add("Viveka")
print(set7)
# The order of elements in the output may not match the order in the original list, as sets are unordered collections. So indexation do not work in set






