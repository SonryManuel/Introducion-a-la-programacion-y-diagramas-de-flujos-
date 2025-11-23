# 1. Edad
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 2. Número positivo, negativo o cero
numero = float(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 3. Par o impar
num = int(input("Introduce un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 4. Nota
nota = int(input("Introduce tu nota (0-100): "))
if nota >= 90:
    print("Aprobado con A")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# 5. Descuento en compra
monto = float(input("Introduce el monto de tu compra: "))
if monto > 500:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"Se aplicó un 10% de descuento. Total a pagar: {total}")
else:
    print(f"Total a pagar: {monto}")