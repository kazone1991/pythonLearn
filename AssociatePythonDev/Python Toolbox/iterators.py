#iterators in Python
#iterators are objects that can be iterated upon, meaning you can traverse through all the values.
#An iterator is an object which implements the iterator protocol, consisting of the methods __iter__() and __next__().
#Iterators are used in for loops, comprehensions, and other contexts where you need to iterate over a sequence of items.
#Iterating over a list
print("Iterating over a list...")
myList = [1,2,3,4,5,6,7,8,9]
for i in myList:
	print(i)

#Iterating over a tuple
print("\nIterating over a tuple...")
myTuple = (1,2,3,4,5,6,7,8,9)
for i in myTuple:
    print(i)

#Iterating over a string
print("\nIterating over a string...")
for letter in 'DataCamp':
	print(letter)

#Iterating over a set
print("\nIterating over a set...")
mySet = {1,2,3,4,5,6,7,8,9}
for i in mySet:
    print(i)

#Iterating over a range
print("\nIterating over a range...")	
for i in range(5):
	print(i)

#Iterating over a dictionary
print("\nIterating over a dictionary...")
myDictionary = {"a":23,"b":21,"c":34,"d":99,"e":45}
for key, value in myDictionary.items():
	print(key, value)

#Iterating over a file
#print("\nIterating over a file...")
#with open('myfile.txt', 'r') as file: 
#    for line in file:
#        print(line.strip())

#Using iter() and next()
print("\nUsing iter() and next()...")
myString = "Hello"
myIterator = iter(myString)
print(next(myIterator))  # Output: H
print(next(myIterator))  # Output: e
print(next(myIterator))  # Output: l
print(next(myIterator))  # Output: l
print(next(myIterator))  # Output: o
#print(next(myIterator))  # Output: # Raises StopIteration error
print(next(myIterator, 'End of String'))  # Output: End of String (no error raised)

#Getting all items from an iterator without next()
print("\nGetting all items from an iterator without next()...")
myText = "Python is great"
myTextIterator = iter(myText)
print(*myTextIterator)  # Output: P y t h o n   i s   g r e a t