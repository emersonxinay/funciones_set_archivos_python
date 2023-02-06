# escribir archivo: r+ = te permite leer y escribir y aumenta los datos que va agregando
# w+ lo sobrescribe
with open('./texto.txt', 'r+') as file:
    for line in file:
        print(line)
    # para sobre escribir
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('nueva linea\n')
