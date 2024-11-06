# ejercicio2.py

nombre = input("¿Cuál es tu nombre? ")
print(f"Nombre en mayúsculas: {nombre.upper()}")
print(f"El nombre tiene {len(nombre)} caracteres.")

for _ in range(len(nombre)):
    print(nombre)
