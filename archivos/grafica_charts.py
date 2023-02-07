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
