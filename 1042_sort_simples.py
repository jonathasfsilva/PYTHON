linha = input().split(" ")

o1, o2, o3 = linha

x = int(o1)
y = int(o2)
z = int(o3)

lista = [x, y, z]
lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print("")
print(x)
print(y)
print(z)