palabra = input("Introduce una palabra o basta para terminar: ")
palabras = []
while palabra.lower() != "basta" and palabra != "":
    palabra = input("Introduce una palabra o basta para terminar: ")
    palabras.append(palabra)
    for palabra in palabras:
        print(palabra, end="")
    print()
print("Has terminado.")
