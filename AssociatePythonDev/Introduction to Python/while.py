#While in Python
# This program will print numbers from 1 to 5 using a while loop
number = 1
while number <= 5:
    print(number)
    number += 1  # Increment the number by 1

# This program will simulate a stock sale until the stock runs out
stock = 10
num_ventas = 0
while num_ventas < stock:
	num_ventas += 1
	print(stock - num_ventas)

#Infinite loop example
# Uncomment the following lines to see an infinite loop
# while True:
#     print("This will run forever unless stopped manually")

#If statement with while loop
stock = 10
num_ventas = 0
while num_ventas < stock:
    num_ventas += 1
    # Conditional statement inside the loop
    if stock - num_ventas > 7:
        print("Plenty of stock remaining")
    elif stock - num_ventas > 3:
        print("Some stock remaining")
    elif stock - num_ventas != 0:
        print("Low stock!")
    else:
        print("No stock!")