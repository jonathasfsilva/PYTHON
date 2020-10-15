import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
lista = [10,20,30]
arr = np.array(lista)
dic = {'a':10, 'b':20, 'c':30}

series = pd.Series(data=lista, index=labels)
print(series)
print(series['b'])

ser1 = pd.Series(data=[1,2,3,4,5], index=['EUA','Brasil','Alemanha','Japao','Canada'])
print(ser1)

ser2 = pd.Series(data=[1,2,3,4,5], index=['EUA','Brasil','Italia','Japao','Canada'])
print(ser1 + ser2)