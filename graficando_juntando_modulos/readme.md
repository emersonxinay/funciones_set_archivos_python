# Comprehencions, funciones, y manejo de errores

## Conjuntos con set
```py
#ejem:
set_countries = {  }
# ---- conjunto de paises en string
set_contries = {'Perú', 'Mexico', 'Bolivia', 'Chile'}
# imprimiendo normal
print(set_contries)
# imprimiendo con tipo de dato
print(type(set_contries))

```

# modulos
```py
import modulos.utils as utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''


if __name__ == '__main__':
    run()
```

# funciones 
```py
def sum(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


# llamando objetos
resultado = sum(1, 10)
resultado2 = sum(10, 100)
print(resultado, 'el otro resultado: \n', resultado2)
```


# manejo de errores
```py 
# resolviendo el error de edad
try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menos de edad')
except Exception as error:
    print(error)

```

# archivos 
```py
# leer el archivo
file = open('./texto.txt')
# # lee todo el archivo
# print(file.read())

# # lee de linea a linea
# print(file.readline())

# aplicando ciclo for
for line in file:
    print(line)
# cerrar archivo
file.close()

# -----> de forma mas pro para abrir y cerrar archivos

with open('./texto.txt') as file:
    for line in file:
        print(line)
```
# leer un csv
</a href="https://www.kaggle.com/"> Kaggle.com - Página para buscar datos </a>

```py
import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        # leer fila a fila
        for row in reader:
            # lo va unir con array con tuplas
            iterable = zip(header, row)
            # print(list(iterable))
            # generando diccionario
            country_dict = {key: value for key, value in iterable}
            # print(country_dict)
            data.append(country_dict)
        return data


if __name__ == '__main__':
    data = read_csv('./population.csv')
    print(data[0])

```

# hacer graficas 
<a href="https://matplotlib.org/"> matplotlib - pagina </a>

## instalar  matplotlib en vscode
```bash
pip install matplotlib
```
### o también la extención 
<a href=" https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview"> matplotlib en vscode </a>

```py
import matplotlib.pyplot as plt

# grafica de barras


def generate_bar_chart(labels, values):

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# grafica de tipo tortas


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 20, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
```

