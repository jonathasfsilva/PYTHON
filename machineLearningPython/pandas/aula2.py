import pandas as pd
import numpy as np

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

#exibindo colunas
print(df[['W','Z']])

#criando colunas
df['nova'] = df['W'] + df['Z']
print(df)

#deletando coluna
"""
axis é o eixo, 1 é vertical e 0 horizontal
essa operação não sobrescreve o DataFrame

duas maneiras de resolver isso:
df = df.drop('nova', axis=1)
ou
df.drop('nova', axis=1, inplace=True)
"""
print(df.drop('nova', axis=1))
df.drop('nova',axis=1, inplace=True)
#encontrando valores
"""
df.loc -> vai estar encontrando valores com o nome das colunas ou linhas
df.iloc -> vai estar encotrando os valores baseado nos indices
"""
print(df.loc['A','W']) #um unico item
print(df.loc['A']) #uma linha
print(df.loc[['A', 'B'],['X', 'Y', 'Z']])#uma fatia
print(df.iloc[1:4,2:])