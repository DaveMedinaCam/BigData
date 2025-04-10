# Operaciones básicas
a = 5
b = 3
suma = a + b
resta = a - b
producto = a * b
division = a / b

print("Operaciones básicas:")
print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {producto}")
print(f"{a} / {b} = {division}")

# Estructura condicional
if suma > 10:
    print("La suma es mayor que 10")
else:
    print("La suma es 10 o menor")

# Bucle for
print("\nTabla del 3:")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# Función simple
def cuadrado(x):
    return x * x

print("\nCuadrados del 1 al 5:")
for i in range(1, 6):
    print(f"El cuadrado de {i} es {cuadrado(i)}")