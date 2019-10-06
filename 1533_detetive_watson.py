while True:
    suspeitos = int(input())
    if suspeitos == 0:
        break
    lista = [int(x) for x in input().split()]
    lista = lista[0:suspeitos]
    ordena = sorted(lista)
    achar = ordena[-2]
    print(lista.index(achar)+1)
