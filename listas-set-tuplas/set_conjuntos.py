# ---- conjunto de paises en string
set_contries = {'Perú', 'Mexico', 'Bolivia', 'Chile'}
# imprimiendo normal
print(set_contries)
# imprimiendo con tipo de dato
print(type(set_contries))


# ---- conjuntos de numeros

set_numbers = {1, 3, 4, 4, 5, 5, 6}
# imprime sin repeticiones
print(set_numbers)

# ----- conjunto de varios tipos de datos

set_types = {1, 'hola', False, 12.3}
print(set_types)

# ----- conjunto usando el set como metodo para string y te imprime aleatoriamente
set_from_string = set('hoooooola mundo')
# los caracteres que se repiten solo se imprime una vez
print(set_from_string)

# ----- conjunto a partir de una tupla
set_from_tuplas = set(('abc', 'as', 'cdv', 'as'))
print(set_from_tuplas)

# ---- conjunto  a partir de una lista
numbers = [1, 2, 3, 4, 5, 6, 5, 2, 3, 2, 3, 2]
# convertimos a conjunto la lista
set_number = set(numbers)
# imprimimos el nuevo conjunto sin repeticiones de  números
print(set_number)
# y ahora si quiero devolver nuevamente a lista sin repeticiones
unique_numbers = list(set_number)
print(unique_numbers)
