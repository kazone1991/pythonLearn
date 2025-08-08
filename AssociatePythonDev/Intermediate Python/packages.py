#packages in python
import pandas as pd

#using pandas to convert a dictionary to a DataFrame
sales = {"user_id": ["KM37", "PR19", "YU88"],"order_value": [197.75, 208.21, 134.99]}
sales_df = pd.DataFrame(sales)
# Display the DataFrame
print(sales_df)

#check types of the DataFrame
print(type(sales_df))

#using pandas to read a CSV file
# Assuming 'sales_data.csv' is a CSV file in the same directory
# sales_df = pd.read_csv('sales_data.csv')
# Display the DataFrame
# print(sales_df)

#heading the DataFrame
print(sales_df.head())