 #pip3 install openpyxl
 #pip3 install xlrd

import pandas as pd
import numpy as np

#Temperaturas
#T01 = Entrada do Evaporador (Ar quente)
#T02 = Saida do Evaporador (Ar resfriado)
#T03 = Descarga Compressor
#T04 = Succao Compressor
#T05 = Da descarga do compressor para a entrada do condesador 
#T06 = Entrada do condensador (Ar temperatura ambiente)
#T07 = Saida do Condesador (Ar aquecido)
#T08 = Ponto para medicao de subresfriamento no condensador

#Pressoes
#P01 = Pressao na descarga
#P02 = Pressao na succao

df = pd.read_excel('test.xlsx', index_col=0, dtype={'DATE':str, 'TIME':str, 'T01':float, 'T02':float, 'T03':float, 'T04':float, 'T05':float, 'T06':float, 'T07':float, 'T08':float, 'P01':float, 'P02':float,}) 

#print(df['P02'][100])

print('T01 = ', round(np.mean(df['T01']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T01']),1), u'\u00B0'+'C')
print('T02 = ', round(np.mean(df['T02']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T02']),1), u'\u00B0'+'C')
print('T03 = ', round(np.mean(df['T03']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T03']),1), u'\u00B0'+'C')
print('T04 = ', round(np.mean(df['T04']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T04']),1), u'\u00B0'+'C')
print('T05 = ', round(np.mean(df['T05']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T05']),1), u'\u00B0'+'C')
print('T06 = ', round(np.mean(df['T06']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T06']),1), u'\u00B0'+'C')
print('T07 = ', round(np.mean(df['T07']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T07']),1), u'\u00B0'+'C')
print('T08 = ', round(np.mean(df['T08']),1), u'\u00B0'+'C', u'\u00B1', round(np.std(df['T08']),1), u'\u00B0'+'C')
print('P01 = ', round(np.mean(df['P01']),1), u'\u00B0'+'K', u'\u00B1', round(np.std(df['P01']),1), u'\u00B0'+'K')
print('P02 = ', round(np.mean(df['P02']),1), u'\u00B0'+'K', u'\u00B1', round(np.std(df['P02']),1), u'\u00B0'+'K')