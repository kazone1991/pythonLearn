#chunks in python
import pandas as pd

#process large files in chunks adding results to a list and then summing to get total
results = []
for chunk in pd.read_csv('file.csv', chunksize = 10000):
    # Process each chunk
    results.append(sum(chunk['column_name']))  # Replace 'column_name' with the actual column name you want to sum

total = sum(results)
print("Total sum of column_name:", total)

#process large files in chunks adding results to a total
totalSum = 0
for chunk in pd.read_csv('file.csv', chunksize=10000):
    totalSum += sum(chunk['column_name'])  # Replace 'column_name' with the actual column name you want to sum

print("Total sum of column_name:", totalSum)
