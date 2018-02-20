menor = 0
maior = 0
a = int(input())
b = int(input())
soma = 0
if a < b:
    menor = a
    maior = b
elif a > b:
    menor = b
    maior = a
while menor <= maior:
    if menor % 13 == 0:
        menor = menor + 1
    else:
        soma = soma + menor
        menor = menor + 1
print(soma)