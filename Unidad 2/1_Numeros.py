print("Dame dos números y te diré cuál es mayor.")
print("Introduzce el primer número:")
num1 = float(input())
print("Introduzce el segundo número:")
num2 = float(input())
if num1 > num2:
    print("El número mayor es: ", num1)
elif num2 > num1:
    print("El número mayor es: ", num2)
elif num1 == num2:
    print("Ambos números son iguales.")