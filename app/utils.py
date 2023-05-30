'''def get_population():
  keys = ['col', 'bol']
  values = [300,400]
  return keys, values'''

def population_by_coutry(data, country):
  country = country.capitalize()
  result =  list(filter( lambda item: item['Country/Territory'] == country, data))
  return result[0]

def population_year(data):
  dict_pop = {key.replace('Population','') : int(data[key]) for key in data if 'Population' in key and 'World' not in key}  
  #dict = {key : value for (key, value) in data.items() if 'Population' in key} #.items separa llave de valor
  dict_pop = dict(sorted(dict_pop.items()))
  return dict_pop.keys(), dict_pop.values()

def get_population_percentage (data):
  countries_percentage = dict(map(lambda item : (item['Country/Territory'], float(item['World Population Percentage'])), data))
  return countries_percentage.keys(), countries_percentage.values()
  
    