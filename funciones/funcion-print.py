# función por defecto de python
print('Hola')

# funcion creada por nosotros


def mi_funcion(text):
    print(f'hola a todos es mi función: {text*2} ')


# llamando mi objeto
mi_funcion('esto viene desde fuera')
mi_funcion('emerson')

mi_funcion('juanita')

# haciendo operaciones matematicas dentro de otra función


def suma(a, b):
    # print normal
    print(a+b)
    # introduciendo función anterior
    mi_funcion(a + b)


# llamando objetos
suma(4, 5)  # 9 y 18 por que la función anterior se multiplica *2
suma(7, 9)  # 16 y 32
