import read_csv
# import nums_from_string
import charts

data = read_csv.read_csv('data.csv')
data = list(filter(lambda country: country['Continent'] == 'South America', data))

percentage = {dat['Country/Territory']:float(dat['World Population Percentage']) for dat in data}

labels = percentage.keys()
values = percentage.values()

charts.generate_pie_chart(labels, values, 'Mundial')