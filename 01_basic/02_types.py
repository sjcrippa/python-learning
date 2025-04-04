# Python es un lenguaje de tipado dinamico
# No es necesario declarar el tipo de variable, se define en tiempo de ejecucion
# Los tipos de datos se asignan en tiempo de ejecucion
# Los tipos de datos se pueden cambiar en tiempo de ejecucion

# Tipos de datos
# int: numeros enteros
# float: numeros decimales
# str: cadenas de caracteres
# bool: booleanos (True o False)
# list: listas
# dict: diccionarios
# tuple: tuplas
# set: conjuntos
# complex: numeros complejos
# None: valor nulo
# type: tipo de dato
# isinstance: verifica si una variable es de un tipo de dato

print("int: ")
print(10)
print(type(10))
print(type(12312354871423895791823234))

print("float: ")
print(10.5)
print(type(10.5))
print(type(12312354871423895791823234.123123123123))

print("complex: ")
print(1+2j)
print(type(1+2j))

print("str: ")
print("Hola")
print(type(" "))
print("Hola" + " " + "Mundo")
print(type("Hola" + " " + "Mundo"))

print("bool: ")
print(True)
print(type(True))

print("None: ")
print(None)
print(type(None))

print("isinstance: ")
print(isinstance(1, int))
print(isinstance(1, str))