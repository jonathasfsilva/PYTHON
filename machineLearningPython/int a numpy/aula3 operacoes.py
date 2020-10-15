import numpy as np

arr = np.arange(0,16)

# somando, multiplicando, subtraindo e dividindo arrays
print(arr + arr)
print(arr * arr)
print(arr - arr)
print(arr / arr)

# operações com escalares
print(arr + 100)
print(arr * 2)
print(1 / arr)

# metodos np
print(np.sqrt(arr))
print(np.exp(arr))
print(np.average(arr))
print(np.std(arr)) # desvio padrao
print(np.max(arr))
print(np.min(arr))
