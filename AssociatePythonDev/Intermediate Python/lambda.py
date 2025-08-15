#lambda functions in python
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not needed elsewhere in the code.
# Syntax: lambda arguments: expression
lambda x: sum(x) / len(x)
print((lambda x: sum(x) / len(x))([1, 2, 3, 4, 5]))  # Output: 3.0

#store lambda function in a variable
average = lambda x: sum(x) / len(x)
print(average([1, 2, 3, 4, 5]))  # Output: 3.0

#multiple arguments in lambda function
lambda x, y: x ** y
print((lambda x, y: x ** y)(2, 3)) # Output: 8

#lambda function with iterables
# Using map to apply a lambda function to each item in an iterable
users = ["alice", "bob", "charlie"]
capitalize = map(lambda x: x.capitalize(), users)
print(capitalize)  # Output: <map object at ...>
print(list(capitalize))  # Output: ['Alice', 'Bob', 'Charlie']

#lambda without arguments
# A lambda function can also be defined without any arguments, but it must still have an expression
no_args = lambda: "Hello, World!"
print(no_args())  # Output: Hello, World!

#lambda function with filter
# Using filter to apply a lambda function to filter items in an iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

#lambda function with reduce
from functools import reduce
# Using reduce to apply a lambda function to reduce an iterable to a single value
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 3628800

#lambda function with sorting
# Using sorted with a lambda function to sort a list of tuples by the second element
data = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]

#lambda function with default arguments
# A lambda function can also have default arguments
default_greet = lambda name="World": f"Hello, {name}!"
print(default_greet())  # Output: Hello, World!
print(default_greet("Alice"))  # Output: Hello, Alice!      

#lambda function with conditionals
# A lambda function can include conditional expressions
conditional_lambda = lambda x: "Even" if x % 2 == 0 else "Odd"
print(conditional_lambda(4))  # Output: Even
print(conditional_lambda(5))  # Output: Odd 


