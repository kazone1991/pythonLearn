#Generator Expressions in Python
# Generator expressions are a concise way to create generators in Python.
# They are similar to list comprehensions but use parentheses instead of square brackets.

# Generator expressions are more memory efficient than list comprehensions
myComprehension = [2 * num for num in range(0,9)] #creates a new list
print(myComprehension)
myGenerator = (2 * num for num in range(0,9)) #creates a generator object
print(myGenerator)

# Generator expressions can be iterated over just like lists
print("Iterating over generator expression: ")
results = (2*num for num in range(0,9))
print(type(results)) #class generator, it is iterable
print(results)
for result in results:
	print(result)

print("Iterating over generator expression with list: ")     
results2 = (num +1 for num in range(9))
print(list(results2))

#Lazy evaluation with generator expressions
print("Lazy evaluation with generator expressions: ")
nums = (num ** 2 for num in range(9))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

#conditional generator expressions
print("Conditional generator expressions: ")
nums = (num ** 2 for num in range(9) if num % 2 == 0)
print(list(nums))

#Generator functions
# Generator functions use the `yield` statement to produce a value and pause execution,
# allowing the function to be resumed later.
# They are defined like regular functions but use `yield` instead of `return`.
# Example of a generator function
def num_sequence(n):
    """Generator function that yields numbers from 0 to n."""
    i = 0
    for num in range(n):
        yield num
        i += 1
    print("Generator function completed.")

# Using the generator function
print("Using the generator function:")
myGeneratorFunc = num_sequence(6)
print(type(myGeneratorFunc)) # It is a generator object
for i in myGeneratorFunc:
	print(i)

# # Create a list of strings: lannister
# lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# lengths = (len(person) for person in lannister)
# for value in lengths:
#     print(value)

# # Create generator object: result
# result = (num for num in range(0,31))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# for value in result:
#     print(value)

# # Create a list of strings
# lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# def get_lengths(input_list):
#     """Generator function that yields the
#     length of the strings in input_list."""
#     # Yield the length of a string
#     for person in input_list:
#         yield len(person)
# print(get_lengths(lannister))
# for value in get_lengths(lannister):
#     print(value)
