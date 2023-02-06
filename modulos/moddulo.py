# modulo para sistema operativo
import collections
import time
import re
import sys
print(sys.path)
# expresiones regulares
text = "mi numero de telefono es 12345678, el codigo de 57, mi numero de la suerte es 5"
# vamos a encontrar del texto solo numeros
result = re.findall('[0-9]+', text)
print(result)

# manejador de horas y fechas
timestamp = time.time()
print(timestamp)

hora_local = time.localtime()
resultado = time.asctime(hora_local)
print(resultado)

# manejador de colecciones : cual es la frecuencia de esta lista
numbers = [1, 1, 2, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 4]
contar_repetidos = collections.Counter(numbers)
print(contar_repetidos)  # ({3: 5, 2: 4, 4: 4, 1: 2})
