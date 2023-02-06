# ---- unión
set_a = {'col', 'pe', 'cl'}
set_b = {'arg', 'mx'}

set_c = set_a.union(set_b)
print(set_c)
# usando operador
print(set_a | set_b)

# ---- inteseccion
set_c = set_a.intersection(set_b)
print(set_c)
# usando operador
print(set_a & set_b)

# ----- la diferencia

set_c = set_a.difference(set_b)
print(set_c)
# usando operador
print(set_a - set_b)

# ----- diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# usando operador
print(set_a ^ set_b)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAm, centralAm, southAm)
# Escribe tu solución 👇

print(new_set)
