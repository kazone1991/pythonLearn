#lists in Python
print("Creating list")
cookies = ['oreo', 'chokis', 'suavicrema']
print("cookies list: ", cookies)

#access element on list
print("\nAccesing element on the list by index")
print(cookies[2])

#append value to a list
print("\nAppending value to list")
cookies1 = ['oreo', 'chokis', 'suavicrema']
print("cookies before append: ", cookies1)
cookies1.append('emperador')
print("cookies after append: ", cookies1)

#combing lists using + operator
print("\nCombining lists using + operator")
cookies2 = ['oreo', 'chokis', 'suavicrema']
print("cookies list: ", cookies2)
cakes = ['submarinos', 'pinguinos']
print("cakes list: ", cakes)
#new list desserts
desserts = cookies2 + cakes
print("new desserts list: ", desserts)

#combining lists using extend function
print("\nCombining lists using extend function")
cookies3 = ['oreo', 'chokis', 'suavicrema']
print("cookies list: ", cookies3)
cakes = ['submarinos', 'pinguinos']
print("cakes list: ", cakes)
cookies3.extend(cakes)
print("cookies extended list: ", cookies3)

#finding elements on list, getting position using index function
print("\nFinding cookie position using index function")
cookies4 = ['oreo', 'chokis', 'suavicrema']
position = cookies4.index('suavicrema')
print("cookies list: ", cookies4, "\ncookie: ", cookies4[2], "\nposition: ", position)

#removing elements from list using pop function
print("\nRemoving element from list using pop function")
cookies5 = ['oreo', 'chokis', 'suavicrema']
print("cookies list before pop: ", cookies5)
cookies5.pop(1)
print("cookies list after pop: ", cookies5)

#iterating over a list with list comprehension
print("\nIterating over a list with list comprehension")
cookies6 = ['oreo', 'chokis', 'suavicrema']
titlecase_cookies = [cookie.title() for cookie in cookies6] #using title function to get value of item
print("the cookies titles are: ", titlecase_cookies)

#sorting a list using sorted function
print("\nSorting a numeric list using sorted function")
myNumericList = [9,2,4,6,7]
print("unsorted list: ", myNumericList)
print("sorted list: ", sorted(myNumericList))

print("\nSorting a alphabetic list using sorted function")
myAlphabeticList = ['Z','B','H','P','X']
print("unsorted list: ", myAlphabeticList)
print("sorted list: ", sorted(myAlphabeticList))