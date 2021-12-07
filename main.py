import csv
import pandas as pd
import requests
from config import URL, ARQUIVO_CSV

response = requests.get(URL)
with open('drinks.csv','w',newline='\n') as novo_arquivo:
   writer = csv.writer(novo_arquivo)
   for linha in response.iter_lines():
       writer.writerow(linha.decode('utf-8').split(','))


arquivo_csv = pd.read_csv(ARQUIVO_CSV)

#print(arquivo_csv.head().to_string())

#print(arquivo_csv['country'])

arquivo_csv = pd.read_csv(ARQUIVO_CSV, usecols=['country','wine_servings'], index_col='country')
print(arquivo_csv)

