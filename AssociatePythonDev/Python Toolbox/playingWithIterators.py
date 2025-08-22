#enumerate and zip functions in python
# Using enumerate to iterate over a list with index
print("Using enumerate....")
students = ["Kevin", "Pedro", "Jose", "Carlos"]
myEnumerator = enumerate(students)
print(type(myEnumerator)) #class enum
myEnumeratorList = list(myEnumerator)
print(myEnumeratorList) # will show a list of tuples with the enumerator values added

#unpacking the enumerator
print("\nUnpacking the enumerator...")
for index, value in enumerate(students):
    print(index, value)

#using start value in enumerate
print("\nUsing start value in enumerate...")
for index, value in enumerate(students, start=10):
    print(index, value)

# Using zip to combine two lists
print("\nUsing zip....")
students = ["Kevin", "Diego", "Juan", "Carlos"]
notes = ["A+", "B+", "A", "B"]
myZip = zip(students,notes)
print(type(myZip)) #Class zip
myZipListed = list(myZip)
print(myZipListed) #(Kevin, A+), (Pedro, B+)

#unpacking the zip
print("\nUnpacking the zip...")
for student, note in zip(students, notes):
    print(student, note)

#using zip with the splat operator
print("\nUsing zip with the splat operator...")
students = ["Kevin", "Pedro", "Jose", "Carlos"]
notes = ["A+", "B+", "A", "B"]
myZip = zip(students, notes)
print(*myZip)

#using zip with different length lists
print("\nUsing zip with different length lists...")
students = ["Kevin", "Diego", "Juan", "Carlos", "Pedro"]
notes = ["A+", "B+", "A", "B"]
for student, note in zip(students, notes):
    print(student, note) #will only iterate until the shortest list ends

#using zip with three lists
print("\nUsing zip with three lists...")
students = ["Kevin", "Diego", "Juan", "Carlos", "Pedro"]
notes = ["A+", "B+", "A", "B"]
age = [18, 19, 20, 21, 22]
for student, note, age in zip(students, notes, age):
    print(student, note, age) #will only iterate until the shortest list ends

#using zip to unzip a list of tuples
print("\nUsing zip to unzip a list of tuples...")
students = ["Kevin", "Diego", "Juan", "Carlos"]
notes = ["A+", "B+", "A", "B"]
age = [18, 19, 20, 21]
zipped = zip(students, notes, age)
print(zipped) #zip object
zippedList = list(zipped)
print(zippedList) #list of tuples
students2, notes2, age2 = zip(*zippedList)
print(students2) #('Kevin', 'Diego', 'Juan', 'Carlos')
print(notes2) #('A+', 'B+', 'A', 'B')
print(age2) #(18, 19, 20, 21)