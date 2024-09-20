# List, append - example:

my_shopping_list = ["bread", "milk", "jam"]
print(my_shopping_list)
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    my_list.append("cheese")
    #more_items = input("Enter the item") # user input
    #my_list.append(more_items)
    # my_list.remove(more_items)
    # my_list.insert(0,more_items)
    # to remove duplicates from the list we use set
    return my_list
l = bring_more_food(my_shopping_list)
print(l)
