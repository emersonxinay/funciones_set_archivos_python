def increment(x):
    return x + 1


""" 
increment2 = lambda x:x+1
"""


def otra_funcion(x, func):
    return x + func(x)


result = otra_funcion(3, increment)
# 3 + (3+1)
print(result)

""" 
# otra forma de hacer solo con lambda
otra_funcion2 = lambda x, func: x +func(x)
result = otra_funcion2(3, increment2)

# y otra forma tambien podría ser
result = otra_funcion2(3, lambda x: x+1 )
"""
