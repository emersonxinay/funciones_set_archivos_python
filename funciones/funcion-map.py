# map es hacer transformaciones a una lista
numbers = [1, 3, 4, 5, 6, 7]
numbers_2 = []

for i in numbers:
    numbers_2.append(i * 2)
print(numbers)
print(numbers_2)

# haciendo con otra versión pero list y map
numbers_3 = list(map(lambda i: i*2, numbers))
print(numbers_3)

# cuando tenemos dos listas

lista1 = [1, 3, 4, 5]
lista2 = [6, 7, 8]
print(lista1)
print(lista2)

result = list(map(lambda x, y: x + y, lista1, lista2))
print(result)
