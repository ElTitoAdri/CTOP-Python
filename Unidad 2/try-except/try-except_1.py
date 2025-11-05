texto = ""

try:
    f = open("archivo2.txt", "r")
    # texto = f.read()
    f.write("Hola, picha")
except IOError as e:
    print("Ocurrió un error: ",e)
else:
    print("Fichero escrito correctamente")
finally:
    f.close()