import read_csv
import nums_from_string
import charts

user = input('Indique el país ').title()
graph = input('¿Gráfico de barras o torta? ')

data = read_csv.read_csv('data.csv')


countr = list(filter(lambda country: country['Country/Territory'] == user, data))

country = countr[0]

#Keys completas
keys_1= [item for item in country.keys() if ' Population' in item]
keys_1.pop()


# keys = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']


def rele_data(country, keys):
  
  values = []
  for item in country.keys():
    
    if item in keys:
      
      values.append(int(country[item]))

  
  #Obtener sólo números de keys (Crea lista por valor)
  keys = list(map(lambda key: nums_from_string.get_nums(key),keys))

  #Sacar números de las listas internas como str para labels
  keys = list(map(lambda key: str(key[0]), keys))

  #Armar diccionario con info relevante
  relevant = {key:value for key, value in zip(keys,values)}
  return relevant

populations = rele_data(country, keys_1)


labels = list(populations.keys())
values = list(populations.values())

if graph.lower() == 'torta':
  charts.generate_pie_chart(labels, values, user)
elif graph.lower() == 'barras':
  charts.generate_bar_chart(labels, values, user)






''' Forma simplificada ingresando datos manual

def populations(country):
  population = {
    '2022': int(country['2022 Population']),
    '2020': int(country['2020 Population']),
    '2015': int(country['2015 Population']),
    '2010': int(country['2010 Population']),
    '2000': int(country['2000 Population']),
    '1990': int(country['1990 Population']),
    '1980': int(country['1980 Population']),
    '1970': int(country['1970 Population'])
  }
  labels = population.keys()
  values = population.values()
  return labels, values

'''