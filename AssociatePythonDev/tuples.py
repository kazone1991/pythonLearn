#tuples in python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(type(my_tuple))

#get item from tuple
print(my_tuple[0])  # Output: apple

#Casting a list to a tuple
my_list = ["apple","banana", "cherry"]
my_tuple = tuple(my_list)
print(my_list, "is now", my_tuple, "of type", type(my_tuple))

#Tuples are immutable
try:
    my_tuple[0] = "orange"  # This will raise an error
except TypeError as e:
    print("Error:", e)

# add items to a tuple
# Tuples are immutable, so you cannot add items directly.
# However, you can concatenate tuples to create a new one.
new_tuple = my_tuple + ("orange",)
print("New tuple after concatenation:", new_tuple)  

#remove items from a tuple
# Tuples are immutable, so you cannot remove items directly.
# However, you can convert to a list, remove the item, and convert back to a tuple.
temp_list = list(my_tuple)
temp_list.remove("banana")
my_tuple = tuple(temp_list)
print("Tuple after removing 'banana':", my_tuple)

# Looping through a tuple
for item in my_tuple:
    print(item)