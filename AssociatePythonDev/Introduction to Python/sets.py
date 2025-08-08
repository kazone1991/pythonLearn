#Set in Python
my_set = {"Kevin", "John", "Adam", "Peter"}
print(my_set)

#Set and Dictionary are similar, but sets do not have key-value pairs
my_set = {"Kevin", "John", "Adam", "Peter", "Kevin"}
my_dict = {"name": "Kevin", "age": 30}
print(type(my_set))
print(type(my_dict))

#Duplicate values are ignored in sets
my_set = {"Kevin", "John", "Adam", "Peter", "Kevin"}
print(my_set)

#Cast a list to a set to remove duplicates
my_list = ["Kevin", "John", "Adam", "Peter", "Kevin"]
my_set = set(my_list)
print(my_list, "are now", my_set, "of type", type(my_set))

#Cannot access set items by index
my_set = {"Kevin", "John", "Adam", "Peter"}
# print(my_set[0]) #This will raise an error

#Sorting a set casts it to a list
my_set = {"Kevin", "John", "Adam", "Peter"}
my_ordered_set = sorted(my_set) #sorted() returns a sorted list
print(my_set, "are now", my_ordered_set, "of type", type(my_ordered_set))

#Add items to a set using add() or update()
my_set = {"Kevin", "John", "Adam", "Peter"}
my_set.add("Mary") #add() adds a single item
print(my_set)
my_set.update(["Sam", "Tom", "Jerry"]) #update() can add multiple items
print(my_set)

#Remove items from a set using remove() or discard()
my_set = {"Kevin", "John", "Adam", "Peter"}
my_set.remove("Adam") #remove() raises an error if item not found
print(my_set)
my_set.discard("Tom") #discard() does not raise an error if item not found
print(my_set)

#Clear a set using clear()
my_set = {"Kevin", "John", "Adam", "Peter"}
my_set.clear()
print(my_set)

#Set operations: union, intersection, difference
set_a = {"Kevin", "John", "Adam"}
set_b = {"Adam", "Peter", "Mary"}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b) #or use set_a.union(set_b)
print("Intersection:", set_a & set_b) #or use set_a.intersection(set_b)
print("Difference (A - B):", set_a - set_b) #or use set_a.difference(set_b)
print("Difference (B - A):", set_b - set_a) #or use set_b.difference(set_a)
print("Symmetric Difference:", set_a ^ set_b) #or use set_a.symmetric_difference(set_b)

#Check subset and superset
set_a = {"Kevin", "John"}
set_b = {"Kevin", "John", "Adam", "Peter"}
print("Set A is subset of Set B:", set_a <= set_b) #or use set_a.issubset(set_b)
print("Set B is superset of Set A:", set_b >= set_a) #or use set_b.issuperset(set_a)    
print("Set A is proper subset of Set B:", set_a < set_b) #or use set_a.issubset(set_b) and set_a != set_b
print("Set B is proper superset of Set A:", set_b > set_a) #or use set_b.issuperset(set_a) and set_b != set_a
print("Set A equals Set B:", set_a == set_b) #or use set_a == set_b
print("Set A not equals Set B:", set_a != set_b) #or use set_a != set_b

#Frozenset: immutable set
my_frozenset = frozenset(["Kevin", "John", "Adam", "Peter"])
print(my_frozenset)
# my_frozenset.add("Mary") #This will raise an error since frozens
