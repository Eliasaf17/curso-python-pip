import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader) #Para obtener el nombre de las columnas
    data = []
    # print(header)
    for row in reader:
      iterable = zip(header, row)
      
      country_dict = {header:row for header, row in iterable}

      # print('*'*15)
      # print(country_dict)
      data.append(country_dict)
  return data

if __name__ == '__main__':  #para usarlo como script
  data = read_csv('data.csv')
  print(data[0])