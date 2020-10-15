import numpy as np

arr = np.arange(0, 30, 3)
print(arr)

# pegando pelo index
print(arr[3])

"""
o funcionamento de arrays numpy é semelhamente a listas

exemplos
arr[2:5]
arr[:4]
arr[1:]
"""

arr[2:] = 100

print(arr)
print()
# arrays bidimencionais
arr = np.arange(50).reshape(5, 10)
arr2 = arr[:2]
arr2[:] = 99  # esse array ainda faz referencia ao antigo
"""
para solucionar esse tipo de questão:
arr2 = arr[:2].copy()
"""
# fatiamento de array bidimencional
print(arr[1:4,5:])

print(arr>50)

