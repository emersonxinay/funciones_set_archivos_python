def message_creator(text):
    # la solución de tienda de tecnología
    match text:
        case "computadora":
            return "Con mi computadora programa en python"
        case "celular":
            return "en mi celular uso para ver redes sociales"
        case "cable":
            return "hay cable magico deportes "
    return "articulo no encontrado "


text = input('Ingrese si quiere, computadra, celular o cable: ')
responde = message_creator(text)
print(responde)
