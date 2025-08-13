#custom functions in python
def average(values):
    """Calculate the average of a list of numbers."""
    if not values:
        return 0
    else:
        #Calculate the average by summing the values and dividing by the count
        average_value = sum(values) / len(values)

        rounded_average = round(average_value, 2)  # Round to 2 decimal places
        return rounded_average

def averageShortFunction(values):
    """Calculate the average of a list of numbers using a shorter function."""
    return round(sum(values) / len(values), 2) if values else 0

# Example usage of the custom average function
my_list = [41.37, 22.13, 37.35, 84.56]
print(average(my_list))  # Output: 46.85
print(averageShortFunction(my_list))  # Output: 46.85

#Save functions to a variable
average_function = average
print(average_function(my_list))  # Output: 46.85


def averageRounded(values, rounded = False):
	if rounded == True:
		#average calculation
		average_value = sum(values) / len(values)
		#rounding average
		rounded_average = round(average_value, 2)
		#return average rounded value
		return rounded_average
	else:
		average_value = sum(values) / len(values) 
		return average_value

# Example usage of the averageRounded function
print(averageRounded(my_list, True))  # Output: 46.85
print(averageRounded(my_list, False))  # Output: 46.85 (not rounded)
print(averageRounded(my_list))  # Output: 46.85 (default is rounded)

#Adding docstrings to the functions
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

#Accessing the docstring
print(add.__doc__)  # Output: Return the sum of two numbers.

#updating the docstring
add.__doc__ = "This function adds two numbers together."
print(add.__doc__)  # Output: This function adds two numbers together.

#adding *args and **kwargs
def add_numbers(*args):
    """Return the sum of all numbers passed as arguments."""
    return sum(args)
print(add_numbers(1, 2, 3, 4))  # Output: 10

#adding keyword arguments
def add_numbers_with_kwargs(**kwargs):
    """Return the sum of all keyword arguments."""
    return sum(kwargs.values())
print(add_numbers_with_kwargs(a=1, b=2, c=3))  # Output: 6 

