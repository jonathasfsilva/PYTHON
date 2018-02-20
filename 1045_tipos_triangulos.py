linha = input().split(" ")

o1, o2, o3 = linha

x = float(o1)
y = float(o2)
z = float(o3)

lista = [x,y,z]

lista.sort(reverse=True)

a = lista[0]
b = lista[1]
c = lista[2]

if a < 0 and b < 0 and c < 0:
    print("NAO FORMA TRIANGULO")
elif a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    elif a ** 2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")