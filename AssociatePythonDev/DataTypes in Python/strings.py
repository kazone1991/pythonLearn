#Strings in python
from shlex import join


my_string = "Hello From Python!"
print(my_string)

#Formatted Strings using f string {var}
print("\nFormatting String")
cookie_name = "Emperador"
cookie_value = "$25.50"
print(f"Las galletas {cookie_name} cuestan {cookie_value}")

#Joining Strings Using .join()
print("\nJoining to string using .join()")
names = ["Kevin", "Karla", "Kenia", "Karim"]
#print(", ".join(names))
print(f"Los nombres son {", ".join(names[0:3])} y {", ".join(names[-1:])}.")

#Matching Parts of a String using startswith()
print("\nMatching parts of a string using startswith()")
my_other_string = "Python"
print("Does Python starts with P? Answer: ", my_other_string.startswith('P'))

#filtering list matching strings using startswith()
print("\nFiltering items from list matching strings")
names = ["Kevin", "Pedro", "Karim", "Kiki", "Eddie", "Joel"]
print(f"All names are: {names}")
filtered_names = [name for name in names if name.startswith('K')]
print(f"Names only with K: {filtered_names}")

#Searching things in string
print("\nSearching things in string")
print(f"Word: Long, Phrase: Life is too Long to be Mad - {"Long" in "Life is too Long to be Mad."}")
print(f"Word: long, Phrase: Life is too Long to be Mad - {"long" in "Life is too Long to be Mad."}")

#Approach to be case insensitive
print("\nAppling lower() to be case insensitive")
print(f"word: long, Phrase: LIFE IS TOO LONG TO BE MAD - {"long" in "LIFE IS TOO LONG TO BE MAD".lower()}")