# Mostrar todos los números pares del 1 al 20 utilizando un bucle en una sola línea, separados por comas.
for i in range(2, 21):
    if i % 2 == 0:
        print(i, end=', ')

print("\n")

pares = [p for p in range(2, 21) if p % 2 == 0]
for i in pares:
    print(i, end=', ')