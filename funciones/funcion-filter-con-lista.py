# filtrando datos con filter: filter no modifica solo saca de acuerdo a la condición que se le da
numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)
print(numbers)
