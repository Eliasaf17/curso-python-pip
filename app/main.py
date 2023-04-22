import utils

data = [
    {
      'country' : 'Colombia',
      'population' : 300
    },
    {
      'country' : 'Bolivia',
      'population' : 200
    }
  ]

def run():  #Para que no ejecute todo cuando importe como modulo
  keys, values = utils.get_population()
  print(keys, values)
  
  
  country = input('Type country ').title()
  result = utils.population_by_country(data, country)
  print(result)

if __name__ == '__main__':
  run()