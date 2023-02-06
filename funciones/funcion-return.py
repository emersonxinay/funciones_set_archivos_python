# de formar tradicional sin función
suma = 0
for x in range(1, 10):
    suma += x
print(suma)

# haciendo con función y usando return


def sum(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


# llamando objetos
resultado = sum(1, 10)
resultado2 = sum(10, 100)
print(resultado, 'el otro resultado: \n', resultado2)
