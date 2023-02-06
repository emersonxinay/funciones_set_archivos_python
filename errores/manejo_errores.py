# manejando errores
""" 
try:
    print(0/0)
except ZeroDivisionError as error:

    print(error)
# capturando el error
try:

    assert 1 != 1, "uno no es iguala 1"
except AssertionError as error:
    print(error)
print('hola')

# resolviendo el error de edad
try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menos de edad')
except Exception as error:
    print(error)

print("pasaron los errores")
"""

# ------> tambien con un solo try

try:
    print(0/0)
    assert 1 != 1, "uno no es iguala 1"
    age = 10
    if age < 18:
        raise Exception('No se permiten menos de edad')
except ZeroDivisionError as error:

    print(error)
# capturando el error


except AssertionError as error:
    print(error)
    print('hola')

# resolviendo el error de edad

except Exception as error:
    print(error)

print("pasaron los errores")
print("pasaron los errores")
