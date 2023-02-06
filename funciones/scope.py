# scope es el alcance para trabajar
price = 100  # varible global

# funcion para incrementar precio


def increment():
    price = 200  # variable local
    price = price + 10
    print(price)


print(price)

increment()
