#  lista y por dentro tengo diccionarios
items = [
    {
        'producto': 'camisa',
        'price': 100
    },
    {

        'producto': 'pantalones',
        'price': 300
    },
    {

        'producto': 'poleras',
        'price': 400
    },

]
# transformar a una lista de numeros de solo los precios
price = list(map(lambda item: item['price'], items))
print(price)

# agregar iva a nuestra lista de diccionarios


def agregar_impuesto(item):
    item['impuesto'] = item['price']*0.19
    return item


new_items = list(map(agregar_impuesto, items))
print(new_items)
