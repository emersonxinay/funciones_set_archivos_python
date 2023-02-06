# [element for element in iterable]

lista = ['lunes', 'martes', 'miercoles',
         'jueves', 'viernes', 'sabado', 'domingo']
nueva_lista = []
# iterar con for
for mivariable in lista:
    nueva_lista.append(mivariable + ' hola')

print(nueva_lista)

# ahora de una forma mas elegante
lista2 = [element + ' hola2' for element in lista]
print(lista2)

# ---- numeros pares con for

numbers = []
for i in range(1, 11):
    print(i)
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)

# ---- numeros en forma elegante con element
numbers2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers2)


# otro ejemplo
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [element for element in numbers if element % 2 == 0]

print('v2 =>', even_numbers_v2)
