# ejercicio5.py

import random

# Generar dos números aleatorios entre 2 y 10
num1 = random.randint(2, 10)
num2 = random.randint(2, 10)

# Preguntar por el resultado
respuesta = int(input(f"¿Cuál es el resultado de {num1} * {num2}? "))

# Verificar la respuesta
if respuesta == num1 * num2:
    print("¡Respuesta correcta!")
else:
    print(f"No es correcta. La respuesta correcta es {num1 * num2}")
