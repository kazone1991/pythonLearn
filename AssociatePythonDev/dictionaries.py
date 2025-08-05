#Dictionary en Python
my_dictionary = {"ACH1": 40, "ACH2": 3, "ACH3": 29, "ACH4": 99}
print("Mi diccionario", my_dictionary)

# Acceso a un valor específico del diccionario
my_subset = my_dictionary["ACH1"]
print("El valor de la llave ACH1 es", my_subset)

# Obtener todas los valores del diccionario
print("Los valores dentro del diccionario son", my_dictionary.values())

# Obtener todas las llaves del diccionario
print("Las llaves dentro del diccionario son", my_dictionary.keys())

# Obtener todos los pares clave-valor del diccionario
print("Los items dentro del diccionario son", my_dictionary.items())

# Actualización de un valor del diccionario
my_dictionary["ACH1"] = 50
print(my_dictionary)

# Añadir un nuevo par clave-valor al diccionario
my_dictionary["ACH3"] = 10
print(my_dictionary)

# Creating a dictionary with a duplicate key
my_dictionary = {"AG32": 10, "AG32": 20, "PL65": 30, "OS31": 15, "KB07": 25, "TR48": 35}
# Print the duplicate key's value
print(my_dictionary["AG32"])
