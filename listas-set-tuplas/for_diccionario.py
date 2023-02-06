# obtener numeros de un rango del 1 al 10 y estos deben tener su numero y elvado al cuadrado
import random
diccionario = {}

for i in range(1, 11):
    diccionario[i] = i**2

print(diccionario)


# ahora de forma mas elegante
dic_nuevo = {i: i*2 for i in range(1, 11)}
print(dic_nuevo)

# ---- teniendo una lista construir un diccionario con clave y valor

paises = ['col', 'pe', 'cl', 'bo', 'ecua']
indice_pais = {}
for pais in paises:
    indice_pais[pais] = random.randint(1, 100)

print(indice_pais)

# ahora de forma mas elegante
indice_pais2 = {pais: random.randint(1, 100) for pais in paises}
print(indice_pais2)

# ---- unir dos listas a un diccionario

names = ['emer', 'vale', 'marco']
ages = [12, 56, 98]
# imprime pero de forma de tupla
print(list(zip(names, ages)))

# ahora de forma mas elegante pero en diccinario
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
