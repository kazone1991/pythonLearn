#Error handling in Python
def average(values):
    try:
        average = sum(values) / len(values)
        return average
    except:
        print("average() accepts list or set, please provide the valid data type.")

print(average([1, 2, 3, 4, 5]))  # Should return 3.0
average("12345") # Should print an error message

#use if else and raise to handle specific exceptions
def average_with_check(values):
    if type(values) in [list, set]:
        average = sum(values) / len(values)
        return average
    else:
        raise TypeError("average() accepts list or set, please provide the valid data type.")

print(average_with_check([1, 2, 3, 4, 5]))  # Should return 3.0
average_with_check("12345")  # Should raise TypeError

# Using try-except to handle specific exceptions
def average_with_try_except(values):
    try:
        if type(values) not in [list, set]:
            raise TypeError("average() accepts list or set, please provide the valid data type.")
        average = sum(values) / len(values)
        return average
    except TypeError as e:
        print(e)
print(average_with_try_except([1, 2, 3, 4, 5]))  # Should return 3.0
average_with_try_except("12345")  # Should print TypeError message

