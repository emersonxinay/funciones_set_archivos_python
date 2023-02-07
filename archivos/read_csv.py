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
