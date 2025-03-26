# Modulo print() nos permite imprimir cualquier informacion en la consola
# Las comillas dobles o simples son opcionales pero a veces dependera de la informacion que queramos imprimir
print("Hello, World!")

print("Python", "es", "genial")
# Por defecto viene un separador que es un espacio, pero se puede modificar si queremos:
print("Python", "es", "genial", sep="-")

# Tambien podemos modificar los saltos de linea, que por defecto son \n:
print("Esto se imprime", end=" ")
print("en la misma linea")

# Tambien podemos imprimir variables
name = "Juan"
age = 25
print("Hola, me llamo", name, "y tengo", age, "años")