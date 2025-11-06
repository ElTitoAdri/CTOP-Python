nombre = str(input("Escribe tu nombre: "))
edad = int(input("Escribe tu edad: "))
estudiante = str(input("Eres estudiante (si/no): "))
if estudiante.lower() == "si":
    estudiante = True
else:
    estudiante = False

print("Tu nombre es:", nombre)
print("Tu edad es:", edad)
print("Eres estudiante:", estudiante)