
'''def get_population():
  keys = ['col', 'bol']
  values = [300,400]
  return keys, values'''

def population_by_coutry(data, country):
  dict_pop = (data.loc[data['Country/Territory']==country,'2022 Population':'1980 Population'].transpose().reset_index())
  dict_pop=dict_pop.sort_values(by=['index']).replace({' Population':''}, regex=True)
  return dict_pop['index'], dict_pop.iloc[:,1]

def get_population_percentage (data):
  #countries_percentage = dict(map(lambda item : (item['Country/Territory'], float(item['World Population Percentage'])), data))  # version sin librerias externas
  countries_percentage = data
  #return countries_percentage.keys(), countries_percentage.values()
  return countries_percentage['Country/Territory'].values, countries_percentage['World Population Percentage'].values # version sin librerias externas
  
    