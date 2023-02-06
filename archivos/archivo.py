# leer el archivo
file = open('./texto.txt')
# # lee todo el archivo
# print(file.read())

# # lee de linea a linea
# print(file.readline())

# aplicando ciclo for
for line in file:
    print(line)
# cerrar archivo
file.close()

# -----> de forma mas pro para abrir y cerrar archivos

with open('./texto.txt') as file:
    for line in file:
        print(line)
