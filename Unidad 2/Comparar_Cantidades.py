# Comparar dos numeros
while True:
    try:
        print("Introduce el primer número:")
        num1 = int(input())
        print("Introduce el segundo número:")
        num2 = int(input())
        break
    except ValueError:
        print("Entrada no válida. Por favor, introduce números válidos.")
if num1 > num2:
    print("El primer número", num1, "es mayor que el segundo número",num2)
elif num1 < num2:
    print("El segundo número", num2, "es mayor que el primer número", num1)
else:
    print("Ambos números son iguales.")