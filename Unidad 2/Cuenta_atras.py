#Cuenta atrás de 5 - 50
import time
print("Introduce un número entre 5 y 50 para iniciar la cuenta atrás:")
while True:
    try:
        numero = int(input())
        if 5 <= numero <= 50:
            break
        else:
            print("Por favor, introduce un número válido entre 5 y 50:")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero entre 5 y 50:")
        print("Iniciando cuenta atrás")
while numero >= 0:
    print("-- ",numero," --")
    time.sleep(1)
    numero -= 1
print("¡Fin!")