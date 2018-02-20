x=int(input())
y=int(input())
soma=0

if x == y:
    print("0")
elif x < y:
    while x < y-1:
        x = x +1
        if x % 2 == 1 or x % 2 == -1:
            soma = soma + x
    print(soma)
elif x > y:
    while x > y+1:
        y = y + 1
        if y % 2 == 1 or y % 2 == -1:
            soma = soma + y
    print(soma)