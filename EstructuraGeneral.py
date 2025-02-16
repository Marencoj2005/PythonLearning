# Comentarios: Usar # para comentarios de una línea

"""
Comentarios multilínea:
Este es un comentario que abarca varias líneas.
"""

# Variables
nombre = "Juan"  # String
edad = 25        # Entero
altura = 1.75    # Float
es_estudiante = True  # Booleano

# Imprimir valores
print("Nombre:", nombre)
print("Edad:", edad)

# Operadores básicos
suma = 5 + 3
resta = 10 - 4
multiplicacion = 6 * 7
division = 8 / 2
modulo = 10 % 3  # Residuo de la división
potencia = 2 ** 3  # Potenciación

# Condicionales
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Bucles
for i in range(5):  # Repite 5 veces
    print(f"Iteración {i}")

while edad < 30:
    print(f"Tienes {edad} años")
    edad += 1

# Funciones
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Ana"))
