while True:
    entrada = input("Ingrese su edad: ")
    edad = int(entrada)

    if edad < 1 or edad > 120:
        print("Edad no válida")
    elif edad >= 1 and edad <= 15:
        print("Eres un niño/a")
        break
    elif edad >= 16 and edad <= 21:
        print("Eres un adolescente")
        break
    elif edad >= 22 and edad <= 35:
        print("Eres joven")
        break
    elif edad >= 36 and edad <= 50:
        print("Eres maduro/a")
        break
    elif edad >= 51 and edad <= 60:
        print("Eres de mediana edad")
        break
    elif edad >= 61 and edad <= 80:
        print("Eres mayor")
        break
    elif edad >= 81 and edad <= 100:
        print("Eres anciano/a")
        break
    elif edad >= 101 and edad <= 120:
        print("Eres centenario/a")
        break
