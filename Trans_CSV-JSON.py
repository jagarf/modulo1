import csv
import json

# Constants to make everything easier
CSV_PATH = './TodasLasNoticias-limit.csv'
JSON_PATH = './TodasLasNoticias.json'
# CSV_PATH = 'C:/Users/Jorge/Desktop/IPN/Diplomados/Herramientas de Big Data/TodasLasNoticias.csv'
# JSON_PATH = 'C:/Users/Jorge/Desktop/IPN/Diplomados/Herramientas de Big Data/TodasLasNoticias.json'

data = {}
milista = ()
# Reads the file the same way that you did
csv_file = csv.DictReader(open(CSV_PATH, 'r'))

# Created a list and adds the rows to the list
json_list = []
for row in csv_file:
    json_list.append(row)

print(json_list[0])

for dato in json_list:
    data = dict(fecha=dato[0],
                titulo=dato[1],
                url=dato[2],
                descripcion=[3],
                categoria=[4])
    milista.append(data)

# print(milista)

# Writes the json output to the file
file(JSON_PATH, 'w').write(json.dumps(json_list))