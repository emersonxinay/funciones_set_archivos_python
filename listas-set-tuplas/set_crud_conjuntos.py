set_contries = {'Perú', 'Mexico', 'Bolivia', 'Chile'}
# leer cantidad de datos del conjunto
size = len(set_contries)
print(size)

# add - agregar un nuevo pais
set_contries.add('argentina')
print(set_contries)
set_contries.add('argentina')
print(set_contries)

# update - actualizar un nuevo dato
set_contries.update({'ecuador', 'brasil', 'uruguay'})
print(set_contries)

# remove - eliminar datos
set_contries.remove('argentina')
print(set_contries)

# discard - eliminar o descartar si ingreso un dato que no exista no salga error
set_contries.discard('francia')
print(set_contries)

# clear - para eliminar todo

set_contries.clear()
print(set_contries)
print(len(set_contries))
