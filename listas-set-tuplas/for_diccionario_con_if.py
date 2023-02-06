import random
paises = ['col', 'pe', 'cl', 'arg', 'bo']
id_paises = {pais: random.randint(1, 100) for pais in paises}
print(id_paises)


# vamos a condicionar que los id solo sean amyores o menores usando if
resultado = {pais: id_pais for (pais, id_pais)
             in id_paises.items() if id_pais > 20}
print(resultado)

# generar diciconario con vocales de un string
text = 'hola a todos'
unicos = {c: text.upper() for c in text if c in 'aeiou'}
print(unicos)
# contar cuantas vocales de cada una hay
unicos = {c: text.count(c) for c in text if c in 'aeiou'}
print(unicos)
