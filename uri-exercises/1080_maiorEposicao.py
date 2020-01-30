lista=[]
n=0
for i in range(100):
    lista.append(int(input()))
    x=(max(lista))
    y=(lista.index(x))
print(x)
print(y+1)