from variables import *
from time import sleep
import csv

def treat_csv(url):
  request = requests.get(url)
  csv_string = request.content.decode('utf')
  sleep(1)
  csv_lido = csv.reader(csv_string.splitlines(), delimiter=',')
  count = 0
  produtos_lista = []

  for row in csv_lido:
    count += 1
    if count <= 5:
      continue
    else:
      if len(row) > 6:
        while len(row) > 6:
          row[2]= row[2]+','+ row[3]
          row.pop(3)

      produtos_lista.append(row)

  return produtos_lista