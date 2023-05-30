import utils
import read_csv 
import charts as plt

def run():
  #option = input('1: Poblaciones de un pais \n2: Porcentaje de poblacion mundial\n')
  #cargamos el CSV en una variable
  countries_iter = read_csv.read_csv('data.csv')
  #if option == '1':
  print('***Poblaciones de un pais***')
  #ingresa el nombre del pais
  country = input('Ingrese pais: ') 
  #Obtiene el diccionario del pais seleccionado
  country_populations = utils.population_by_coutry(countries_iter, country)
  #extrae las poblaciones y años.
  keys, values = utils.population_year(country_populations)   
  #grafica 
  plt.generate_bar_chart(country, keys, values)
  #else:
  print('***Porcentaje de poblacion mundial***')
  filtered = list(filter( lambda key :  key['Continent'] == 'South America', countries_iter))
  keys, values = utils.get_population_percentage(filtered)
  plt.generate_pie_chart(keys, values)
  
if __name__ == '__main__':
  run()