""" List """
# 1. List is a collection of items (duplicate is allowed)
# 2. List is mutable(changeable) in nature. Eg, we can replace/reassign the values [0] = _
# 3. List uses more memory
# 4. List uses [] square brackets
# 5. Dynamic data
shopping_list = ["bread", "milk", "butter"]
my_list1 = [1, 2, 3, 4]
my_list2 = ["viveka", 1, 3.14, True]

print(shopping_list)
print(my_list1)
print(my_list2)

print(len(my_list2)) # prints no of values, as per list
print(my_list2[0]) # prints index value of 0

a = "viveka" #variable
print(len(a)) # prints no of letters/places taken

# To replace the value
list1 = [1, 2, 3, 4, 5]
list1[0] = "pramod" #replace
print(list1)
print(list1[0])

list2 = [1, 2, 3, 4]
list2[1] = "dutta"
list2[2] = "dutta" # list allows duplicates
print(list2) # prints all the values
print(list2[1], list2[2]) # prints only the particular index values

# to print the values line by line
for element in list2: #we have used the name of list, since we are working with list directly
    print(element)

# range(1,10) -> range by itself a list, it gives output (1,2,3,4,5,6,7,8,9). If we have a list, then we can directly utilise the name of the list

# To add single value to the existing list, append adds values to the end of the list
list2.append(5) #append accepts only one argument/value, if we want to add more values, we have to repeat the code with different values or repetitive values
print(list2)
# To add multiple values to the existing list, using single code use extend([])
list2.extend([6, 7, 8])
print(list2)
# To insert value inbetween the list, inserts the value before the mentioned index number and shifts the remaining values
list2.insert(4, "pramod") # mention the index value and add the value
print(list2)
# To remove single element from the list, mention the element inside (), to remove multiple elements from the list then we need to use for loop
list2.remove(8) # if we want to remove string mention the value inside double quotes "pramod"
print(list2)
# To reverse the output
list2.reverse()
print(list2)

# To sort the elements
list3 = [1, 6, 2, 8, 5, 4, 7, 3, 9, 3.14, 1.0, 8.9]
list3.sort() # this will sort the values and gives output in ascending order
print(list3)

list3.sort(reverse=True) # this will sort the values and gives output in descending order
print(list3)

# To remove multiple elements from the list, we should use for loop
list4 = [1, 2, 3, 4, 5, 6]
for i in list4:
    if i >= 5:
        pass
    else:
        print(i)

# To concatenate the list
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)


""" When to use List and when to use Range"""
# If we want to print something line by line, and if it's other than list then we can use range with 'for'
# If we want to print something line by line, and if it's list by itself then we can use list name with 'for'




