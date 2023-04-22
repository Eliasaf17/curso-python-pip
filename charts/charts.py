import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots() #Obtener las coordenadas y la figura
    ax.pie(values, labels=labels)   #Asignar los datos para la gráfica
    plt.savefig('pie.png')   #Guarda la gráfica generada como imagen
    plt.close()