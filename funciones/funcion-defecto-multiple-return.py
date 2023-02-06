# creando función
def find_volume(length=1, width=2, depth=2):
    # retornando multiples  valores
    return length * width * depth, width, 'hola a todos'


resultado = find_volume(10, 20, 30)
print(resultado)

print('aqui empieza el de multiples resultados')
# tambien puedes retornar de la siguiente manera
resultado2, ancho, texto = find_volume(length=20)
# imprimiendo los resultados
print(resultado2)
print(ancho)
print(texto)
