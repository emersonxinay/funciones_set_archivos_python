# recuerda que este archivo puede llamarse main.py
# llamando otro modulo
import modulos_crear
key, values = modulos_crear.get_population()
print(key, values)
# lista con diccionario
data = [
    {
        'Country': 'Colombia',
        'Population': 400
    },
    {
        'Country': 'Perú',
        'Population': 500
    },
    {
        'Country': 'Chile',
        'Population': 300
    }
]
# haciendo dinamicamente
country = input('Tipo de country: ')
result = modulos_crear.population_by_country(data, country)
print(result)
