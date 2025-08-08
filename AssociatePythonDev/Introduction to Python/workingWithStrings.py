
#String variable with double quotes
my_string = "Hello using double quotes"
my_other_string = 'Hello using single quotes'

#Using double quotes to use special aposthrophe character
my_message = "don´t use single quotes to type this"
#This is a bad use my_new_message = 'don't use single quotes to type this'

print(my_string)
print(my_other_string)
print(my_message)

#Using triple quotes for multi-line strings
my_big_text = """This is a big sentence that is written in a multi-line.
you can use this to create readable text,
Also use it to format the text, don´t need to use backslash.
"""
print(my_big_text)

#String methods
#Lowercase conversion
my_string = "Hello From Python World!"
my_string = my_string.lower()
print(my_string)

#Uppercase conversion
my_string = "Hello Again From Python World!"
my_string = my_string.upper()
print(my_string)

#Replacing text
my_string = "Hello Kevin, welcome to Python World!"
my_string = my_string.replace("Kevin", "Blazing Craftsman")
print(my_string)