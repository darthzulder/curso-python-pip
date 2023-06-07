import utils
import read_csv 
import charts as plt
import pandas as pd

def run():
  #option = input('1: Poblaciones de un pais \n2: Porcentaje de poblacion mundial\n')

  #cargamos el CSV en una variable
  #countries_data = read_csv.read_csv('data.csv') # version sin librerias externas
  countries_data = pd.read_csv('data.csv')
  #if option == '1':
  print('***Poblaciones de un pais***')

  #ingresa el nombre del pais
  country = input('Ingrese pais: ') 

  #Obtiene el diccionario del pais seleccionado
  #country_populations = utils.population_by_coutry(countries_data, country) # version sin librerias externas
  country_populations =  countries_data[countries_data['Country/Territory'] == country].values
  #extrae las poblaciones y años.
  keys, values = utils.population_by_coutry(countries_data, country)  

  #grafica 
  plt.generate_bar_chart(country, keys, values)
  #else:
  print('***Porcentaje de poblacion mundial***')
  #filtered = list(filter( lambda key :  key['Continent'] == 'South America', countries_data)) # version sin librerias externas
  filtered = countries_data[countries_data['Continent'] == 'Asia']
  keys, values = utils.get_population_percentage(filtered)
  plt.generate_pie_chart(keys, values)
  
if __name__ == '__main__':
  run()