import numpy as np

matriz = [[1,2,3],[3,2,1],[5,4,3]]
print(np.array(matriz))

arr = np.arange(0,10)
print('arrange\n',arr)

arr = np.zeros(3)
print('array de zeros\n',arr)

arr = np.zeros([3,3])
print('matriz de zero\n')

arr = np.ones([5,3])
print('matriz de 1s\n',arr)

arr = np.eye(5)
print('matriz identidade\n',arr)

arr = np.linspace(0,15,5)
print('linspace\n',arr)

#distribuição uniforme
arr = np.random.rand(10)*100
print(arr)

arr = np.random.rand(5,4,3)*100
print('matriz random\n',arr)

arr = np.random.randn(5,4,3)*100
print('matriz random2\n',arr)

arr = np.random.randn(5)
print('randn\n',arr)

arr = np.random.randint(0,100,10)
print('randint\n',arr)


#transformando um array em matriz usando reshape
arr = np.random.rand(25) #array com 25 elementos
arr = arr.reshape((5,5)) #transformação
print(arr)

#mostrando o tamanho de um array
print(arr.shape)

print(arr.max(), arr.argmax()) #o máximo e a posicao
print(arr.min(), arr.argmin()) #mínimo e a posicao
