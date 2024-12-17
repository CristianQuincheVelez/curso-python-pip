import matplotlib

matplotlib.use('Agg')  # Usa un backend sin interfaz gráfica
import matplotlib.pyplot as plt

# Código para graficar
def generate_bar_chart(name,labels,values):
    fig, ax =plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./imagenes/{name}.png')  # Guarda el gráfico en el archivo 'grafico.png'

def generate_pie_chart(labels,values):
    fig, ax =plt.subplots()
    ax.pie(values, labels =labels)
    ax.axis('equal')
    plt.savefig('grafico2.png')  # Guarda el gráfico en el archivo 'grafico.png'


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values =[10,40,80]
    #generate_bar_chart(label,values)
    generate_pie_chart(labels, values)


# Si no necesitas mostrar el gráfico, no pongas plt.show() en el código





