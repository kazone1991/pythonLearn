#built-in functions in Python
print("Hello, World!")  # print function

# Type checking function
print(type(5))
print(type(5.2))
print(type(True))
print(type("Hello"))
print(type([1,2,3]))
print(type({"a":1,"b":2}))
print(type({1,2,3}))
print(type(("apple", "banana")))

#range function
x = range(1,5) # Create a range object from 1 to 4
print(x)  # Print the range object
for i in range(1,5):
	print(i)

#max function
my_list = [41.373,22.135,37.354,84.564]
print(max(my_list))

#min function
#my_list = [41.37,22.13,37.35,84.56]
print(min(my_list))

#sum function
#my_list = [41.37,22.13,37.35,84.56]
print(sum(my_list))

#round function
print(round(3.14159, 2))  # Round to 2 decimal places
print(round(3.14159))  # Round to the nearest integer

#nested functions
total_sales = round(sum(my_list), 2)  # Sum and round the total sales
print(total_sales)

#len function
print(len(my_list))  # Length of the list
print(len("Hello, World!"))  # Length of the string
print(len({"a":1, "b":2, "c":3}))  # Length of the dictionary
print(len({1, 2, 3, 4}))  # Length of the set
print(len((1, 2, 3, 4)))  # Length of the tuple 
print(len(range(1, 10)))  # Length of the range object
#print(len(b"Hello"))  # Length of the bytes object
#print(len(bytearray(b"Hello")))  # Length of the bytearray object
#print(len(memoryview(b"Hello")))  # Length of the memoryview object

#sorted function
print(sorted(my_list))
print(sorted("Kevin"))

#sorted function with reverse order
print(sorted(my_list, reverse=True))

#sorted function with custom key
print(sorted(my_list, key=lambda x: -x))  # Sort in descending order using a custom key

#sorted function with a dictionary
my_dict = {"a": 3, "b": 1, "c": 2}
print(sorted(my_dict.items(), key=lambda x: x[1]))  # Sort dictionary by value
print(sorted(my_dict.items(), key=lambda x: x[0]))  # Sort dictionary by key

#sorted function with a set
my_set = {3, 1, 2}
print(sorted(my_set))  # Sort set elements  

#sorted function with a tuple
my_tuple = (3, 1, 2)
print(sorted(my_tuple))  # Sort tuple elements

#sorted function with a range
my_range = range(1, 5)
print(sorted(my_range))  # Sort range elements  

#help function
#help(sorted) # Display help information for the sorted function

#sum function with a loop
my_list = [41.37,22.13,37.35,84.56]
total_sum  = 0 #init a variable to store result
for i in my_list:
	total_sum = total_sum + i
	print(total_sum)
print("result is", total_sum)