# -*- coding: utf-8 -*-
"""API Generate Rank CSV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zjfRyjfYVkA3q8BKxMyJm_9hovfL6BQC
"""

import pandas as pd

import requests
from time import sleep
import csv







#tratar csv



lista_tratada = tratando_csv(urlAmazon)
emEstoque_df = pd.DataFrame(lista_tratada, columns=['COD. INTERNO', 'COD. EAN', 'DESC', 'SEÇÃO', 'VENDAS', 'LOJA'])



#contando o total de linhas
total_linhas = emEstoque_df['COD. EAN'].count()
#contador
count = 0
loja = ''

# retirando o índice
emEstoque_df = emEstoque_df.iloc[:].rename_axis(None, axis=1)
emEstoque_df.set_index('COD. INTERNO',inplace = True)
emEstoque_df = emEstoque_df.drop(emEstoque_df.index[-1])

emEstoque_df['VENDAS'] = emEstoque_df['VENDAS'].astype(float)
emEstoque_ordenado = emEstoque_df.sort_values('VENDAS', ascending=False)

curva_a = round(total_linhas * 0.2)
curva_b = round(total_linhas * 0.3)
curva_c = round(total_linhas * 0.5)

contador_curvas = 0
curva = []

while contador_curvas < curva_a:
  curva.append('A')
  contador_curvas += 1
while contador_curvas < curva_a + curva_b:
  curva.append('B')
  contador_curvas += 1
while contador_curvas <= total_linhas:
  curva.append('C')
  contador_curvas += 1

emEstoque_ordenado['CURVA'] = curva
emEstoque_ordenado.to_csv(f'rank-{bucket}-{hora_data}.csv', sep=';')
emEstoque_ordenado