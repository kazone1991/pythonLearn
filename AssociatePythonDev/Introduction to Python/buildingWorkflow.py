#in Clause python
products_dict = {"AG32": 10, "HT91": 20, "PL65": 30, "OS31": 15, "KB07": 25, "TR48": 35}
if "OS31" in products_dict.keys():
	print(True)
else:
	print(False)

#not in Clause python
if "OS31" not in products_dict.keys():
	print(False)
else:
	print(True)
	
#increment and decrement variables
sales_count = 0
for sale in range(1, 10):
	# sales_count = sales_count + 1 
	sales_count += 1
	print(sales_count, "increasing..")
stock = 10
for sale in range(1, 10):
	# sales_count = sales_count - 1 
	stock -= 1
	print(stock, "descresing..")
	
#append to list
# Create an empty list
expensive_products = []
# Loop through the dictionary
for key, val in products_dict.items():
	# Check if price is 20 dollars or more
	if val >= 20:
	# Append the product ID to the list 
		expensive_products.append(key)
print(expensive_products)