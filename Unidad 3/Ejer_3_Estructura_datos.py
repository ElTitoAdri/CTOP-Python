frutas = ["manzana", "platano", "cereza", "pera", "naranja"]
print("La primera fruta es:", frutas[0])
print("La ultima fruta es:", frutas[-1])

print("Numero total de frutas:", len(frutas))

print("Introduce el nombre de una fruta para agregar a la lista:")
nueva_fruta = input()
frutas.append(nueva_fruta)
print("Lista actualizada de frutas:", frutas)