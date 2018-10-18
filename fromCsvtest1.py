import pandas as pd 
import os
import csv

headers = {}
conditionalHeaders = 0
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'AndromacoContenido.csv'))

###########################
#Prueba: Crear un diccionario para luego ser creadas 2 listas para ser usadas en melt
#    1. Para id_vars
#    2. Para value_var
for i in df:
    headers[conditionalHeaders] = i
    conditionalHeaders+=1
print(headers[7])
id_vars_list = []
value_vars_list = []
for i in headers:
    if i <= 4:
        id_vars_list.append(headers[i])
    else:
        value_vars_list.append(headers[i])
print(value_vars_list)
print(id_vars_list)
############################


tableUnpivot = pd.melt(df, id_vars=id_vars_list, value_vars=value_vars_list)
tableUnpivot.to_csv(os.path.join(os.path.dirname(__file__), 'nuevo.csv'), header=True)


############################
#Filtro: Se crea un nuevo csv con filtro en los valores verdaderos de la columna Value creada luego del unpivot
with open(os.path.join(os.path.dirname(__file__), 'nuevo.csv'), 'r') as inputCSV, open(os.path.join(os.path.dirname(__file__), 'nuevoNuevo.csv'), 'w') as outputCSV:
    outputCSV = csv.writer(outputCSV)
    inputCSV = csv.reader(inputCSV)
    for row in inputCSV:
        if row[4] == 'verdadero':
            outputCSV.writerow(row)
############################

