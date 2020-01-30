"""dupla = input().split(" ")

x, y = dupla
maior = 0
menor = 0
i = 0
soma = 0
while int(x) >= 0 or int(y) >= 0:

    if int(x) > int(y):
        maior = int(x)
        menor = int(y)
        i = menor
        while i <= maior:
            print(i,"",end="")
            i = i + 1
            soma = i + soma
        print("Sum={}".format(soma-3))
        soma = 0

    elif int(y) > int(x):
        maior = int(y)
        menor = int(x)
        i = menor
        while i <= maior:
            print(i, "", end="")
            i = i + 1
            soma = i + soma
        print("Sum={}".format(soma-3))
        soma = 0



    dupla = input().split(" ")
    x, y = dupla"""


while True:
    try:
        m,n = list(map(int,input().split()))
        if(m < 1 or n < 1 ):
            break
        tmp = 0

        if(m > n):
            tmp = m
            m = n
            n = tmp
        soma = 0
        resultado = ''
        while(m <= n):
            resultado += str(m) + ' '
            soma += m
            m += 1
        resultado += 'Sum=%d'
        print(resultado %soma)
    except:
        break