import matplotlib.pyplot as plt


def generate_bar_chart(labels, values, country):
  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  ax.set_title(f'Crecimiento poblacional {country}', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
  plt.savefig(f'./imgs/{country}.png')
  plt.close()

def generate_pie_chart(labels, values, country):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  ax.set_title(f'Crecimiento poblacional {country}', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 40, 800]
  # generate_bar_chart(labels, values)
  generate_bar_chart(labels, values)