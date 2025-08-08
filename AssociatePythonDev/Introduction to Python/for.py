#For loop in python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in my_list:
    print(i)

#Conditional statements in for loop
prices = [9.99, 8.99, 35.25, 1.50, 5.75]
for price in prices:
	#check is price is more than 10
	if price > 10:
		print("More than $10")
	#check if price is less than 5
	elif price < 5:
		print("Less than $5")
	#Other price
	else:
		print(price)
		
#For in String
my_string = "Hello World!"
for char in my_string:
    print(char)

#For in Dictionary
products = {"AG32":87.99, "HT91":21.50,"PL65":43.75, "OS31":19.99,"KB07":62.95, "TR48":98.0}
for i in products.items():
	print(i)
	
#For in Dictionary with key and value
products1 = {"AG32":87.99, "HT91":21.50,"PL65":43.75, "OS31":19.99,"KB07":62.95, "TR48":98.0}
for key, value in products1.items():
	print(key, value)

#For in Dictionary keys
products2 = {"AG32":87.99, "HT91":21.50,"PL65":43.75, "OS31":19.99,"KB07":62.95, "TR48":98.0}
for key in products2.keys():
	print(key)

#For in Dictionary values
products3 = {"AG32":87.99, "HT91":21.50,"PL65":43.75, "OS31":19.99,"KB07":62.95, "TR48":98.0}
for value in products3.values():
    print(value)

#For in range
for i in range(1,6):
	print(i)

#For in range with step
for i in range(1, 11, 2):
    print(i)

#For in range with negative step
for i in range(10, 0, -1):
    print(i)

#For in range with increment
#Count visits
#This code counts the number of visits to a website
#and prints the total number of visits
visitas = 0
for i in range(1,11):
	#increment visits
	visitas += 1
print("Visits", visitas)
