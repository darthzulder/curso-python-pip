import csv

def read_csv(path):
  i=0
  with open(path, 'r') as csvfile:
    # crea un iterable de listas en formato csv
    reader = csv.reader(csvfile, delimiter = ',')
    #iterar la primera fila donde se encuentra la cabecera, retorna una lista y lo guarda en la variable header
    header = next(reader)
    #declara lista que contendra los diccionarios
    data_concat=[]

    #ciclo para iterar las filas del CSV
    for row in reader:
      #unimos con ZIP las fila de cabezera (llaves) con la fila con contenido, esto da in Objeto iterable, no es lista ni tupla ni diccionario
      iterable = zip(header, row)
      #dictionary comprencion, in dicamos el formato key:value para las variables que estamos declarando para los dos filas en 'iterable', esto lo vuelve un diccionario
      country_dict = {key : value for key, value in iterable}
      #se agrega cada diccionario a la lista.
      data_concat.append(country_dict)
      #print(data_concat[0])
    return data_concat

#permite ejecutar desde terminal, dado que esta dentro de una carpeta o paquete.
if __name__ == '__main__':
  read_csv('./app/data.csv')