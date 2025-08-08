#Comparision Operators
#equal operator
print("equal operator")
print(2 == 2, "2 is equal to 2")
print(2 == 3, "2 is not equal to 3")

#not equal operator
print("not equal operator")
print(2 != 2, "2 is equal to 2")
print(2 != 3, "2 is not equal to 3")

#minor than operator
print("minor than operator")
print(2 < 1, "2 is not less than 1")
print(2 < 2, "2 is not less than 2")
print(2 < 3, "2 is less than 3")

#minor than or equal operator
print("minor than or equal operator")
print(2 <= 1, "2 is not less than or equal to 1")
print(2 <= 2, "2 is less than or equal to 2")
print(2 <= 3, "2 is less than or equal to 3")

#greater than operator
print("greater than operator")
print(2 > 1, "2 is greater than 1")
print(2 > 2, "2 is not greater than 2")
print(2 > 3, "2 is not greater than 3")

#greater than or equal operator
print("greater than or equal operator")
print(2 >= 1, "2 is greater than or equal to 1")
print(2 >= 2, "2 is greater than or equal to 2")
print(2 >= 3, "2 is not greater than or equal to 3")

#Logical Operators
print("Logical Operators")
print((5 > 3) and (3 < 5), "5 is greater than 3 and 3 is less than 5")
print((5 > 3) or (3 > 5), "5 is greater than 3 or 3 is greater than 5")
print(not(5 > 3), "not(5 is greater than 3)")

#if statement in python
print("if statement")
if 5 > 3:
    print("5 is greater than 3")
else:
    print("5 is not greater than 3")

#elif statement in python
print("elif statement")
if 5 > 3:
    print("5 is greater than 3")
elif 5 < 3:
    print("5 is less than 3")
else:
    print("5 is equal to 3")

