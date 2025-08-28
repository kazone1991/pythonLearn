#tuples in Python
#Creating a tuple using ()
print("Creating a tuple using ()")
flavor = 'vainilla', 'chocolate'
print(type(flavor), flavor)

#Zipping tuples using zip()
print("\nZipping tuples using zip()")
us_cookies = ['oreo', 'chip a joy', 'crackers']
print("US Cookies: ", us_cookies)
mx_cookies = ['trikitrakes', 'chokis', 'suavicremas']
print("MX Cookies: ", mx_cookies)
cookies_pairs = zip(us_cookies, mx_cookies)

print("Cookies Pairs zip object: ", cookies_pairs)

#To print the values of a zipped we need to cast to list or tuple as zip() creates a zip object instead of a iterable object.
print("\nCasting zip to a tuple")
listed_cookies = list(cookies_pairs) # this will consume the zip object, cannot be used after this
print("Cookies Pairs from list: ", listed_cookies)

print("\nCasting zip to a tuple") # in order to show zip to tuple the zip needs to be created again
cookies_pairs_again = zip(us_cookies, mx_cookies)
tuple_cookies = tuple(cookies_pairs_again) # this for me looks like a tuple of tuples XD
print("Cookies Pairs from tuple: ", tuple_cookies)

#Unpacking tuples in multiple variables
print("\nUnpacking tuples in multiple variables")
first_us_cookie, first_mx_cookie = listed_cookies[0]
print("Top US Cookie: ", first_us_cookie)
print("Top MX Cookie: ", first_mx_cookie)

#Unpacking tuples using a for loop
print("\nUnpacking tuples using a for loop")
another_cookies_pairs = zip(us_cookies, mx_cookies)
for us_cookie, mx_cookie in another_cookies_pairs:
    print("US Cookie: ", us_cookie)
    print("MX Cookie: ", mx_cookie)

#Enumerating tuples using enumerate()
print("\nEnumerating tuples using enumerate()")
last_cookies_pairs = zip(us_cookies, mx_cookies)
for idx, item in enumerate(last_cookies_pairs):
    us_cookie, mx_cookie = item
    print(f"Cookie position: {idx}, US Cookie: {us_cookie}, MX Cookie: {mx_cookie}")

#Creating tuple by error
print("\nCreating tuple by error")
notATuple = 'value',
print(type(notATuple), notATuple)