# cada vez que hay un error el programa se cierra
# ---- ejemplos
# print(0/0)
# print(result)
""" 
suma = lambda x,y: x+y 
assert suma(2,2)==4
"""

age = 10
if age < 18:
    raise Exception('no se permite menores de edad')
