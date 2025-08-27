def num_sequence(n):
	#generates values from 0 to n
	i = 0
	while i < n:
		yield i
		i += 1
		
results = num_sequence(6)
print(type(results))
for i in results:
	print(i)