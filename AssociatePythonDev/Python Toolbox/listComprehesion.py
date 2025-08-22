#list comprehension in python
# list comprehension is a concise way to create lists in Python
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
print("List without list comprehension")
nums = [12,22,32,42,52]
new_nums = []
for num in nums:
	new_nums.append(num + 1)
print(new_nums)

print("\nList with list comprehension")
nums2 = [12,22,32,42,52]
new_nums2 = [num+1 for num in nums2]
print(new_nums2)

print("\nCreate a list of numbers from 0 to 9 using list comprehension")
myListComprehension = [i for i in range(0,9)]
print(myListComprehension)

#Nested list comprehension
print("\nNested loop to create pairs of numbers")
pairs = []
for i in range(0,2):
	for j in range(6,8):
		pairs.append((i, j))
print(pairs)

print("\nNested list comprehension to create pairs of numbers")
pairs2 = [(i,j) for i in range(0,2) for j in range(6,8)]
print(pairs2)

# Create list comprehension: squares
print("\nList Comprehension Examples create a list of squares from 0 to 9 using list comprehension")
squares = [ i*i for i in range(0,10)]
print(squares)

# Create a 5 x 5 matrix using a list of lists: matrix
print("\nCreate a 5 x 5 matrix using a list of lists")
matrix = [[col for col in range(0,5)] for row in range(0,5)]
# Print the matrix
for row in matrix:
    print(row)

# Create a list of strings: fellowship
print("\nCreate a list of strings using list comprehension")
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# Create a list of strings: fellowship
print("\nCreate a list of strings using list comprehension with condition")
fellowship2 = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship2 = [member if len(member) >= 7 else "" for member in fellowship2]
print(new_fellowship2)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = {member: len(member) for member in fellowship}
print(new_fellowship)

#Conditional list comprehension
print("\nConditional list comprehension to create a list of even numbers from 0 to 9")
nums = [num for i in range(0,9) if num % 2 == 0]
print(nums)

print("\nConditional list comprehension to create a list of squares of even numbers from 0 to 9")
nums2 = [num2 ** 2 for num2 in range(0,9) if num2 % 2 == 0]
print(nums2)

print("\nConditional list comprehension to create a list of numbers from 0 to 9 with even numbers incremented by 1")
nums3 = [num3 + 1 if num3 % 2 == 0 else num3 for num3 in range(0,9)]
print(nums3)

#Dictionary comprehension
print("\nCreate a dictionary using dictionary comprehension from 0 to 9 with values as negative numbers")
myDict = {num: -num for num in range(0, 9)}
print(type(myDict), myDict)

############### other code examples #####################
# Create a list of tuples: tuples
print("\nCreate a list of tuples using list comprehension")
tuples = [(i, j) for i in range(0, 3) for j in range(0, 3)]
# Print the list of tuples
print(tuples)

# Create a list of tuples with even numbers and their squares
print("\nCreate a list of tuples with even numbers and their squares")
even_tuples = [(i, i*i) for i in range(0, 21) if i % 2 == 0]
# Print the list of even tuples
print(even_tuples) 

# Create a list of strings with the first letter capitalized
print("\nCreate a list of strings with the first letter capitalized")
words = ['hello', 'world', 'python', 'list', 'comprehension']
capitalized_words = [word.capitalize() for word in words]
# Print the list of capitalized words
print(capitalized_words)