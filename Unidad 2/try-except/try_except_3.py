while True:
    numero = input("Introduce un numero: ")
    try:
        numero = float(numero)
        print("Has introducido el numero : ", numero)
        break
    except ValueError:
        print("No has introducido un numero valido. Intentalo de nuevo.")