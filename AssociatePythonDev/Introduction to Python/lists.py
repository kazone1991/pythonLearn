#Lists variable
my_list = [1,2,3,4,5,6]
print(my_list)

#subset of the list
#first element
my_subset = my_list[0]
print("First element on the list is", my_subset)

#last element
my_subset = my_list[-1]
print("Last element on the list is", my_subset)

#get a range of elements
my_subset = my_list[0:3]
print("Elements from the list", my_subset)

#get a range of elements including last element in range
my_subset = my_list[0:3 + 1]
print("Elements from the list including last in range", my_subset)

#get a range of elements using slicing
#first three elements
my_subset = my_list[:3]
print("First three element from the list are", my_subset)

#from the third element to the end
my_subset = my_list[2:]
print("Elements from third index onwards are", my_subset)

#using the step argument
#every second element
my_subset = my_list[::2]
print("Every second element from the list", my_subset)

#using the step argument with a negative value
#every second element in reverse order
my_subset = my_list[::-2]
print("Every second element from the list in reverse order", my_subset)

#adding elements to the list
#append method
my_list.append(7)
print("List after appending 7:", my_list)       

#insert method
my_list.insert(0, 0)
print("List after inserting 0 at the beginning:", my_list)  

#extend method
my_list.extend([8, 9])
print("List after extending with [8, 9]:", my_list) 

#removing elements from the list
#remove method
my_list.remove(9)