n1 = 0
n2 = 0

while n1 == 0:
    n = float(input())
    if 0 <= n <= 10:
        n1 = n
    else:
        print("nota invalida")

while n2 == 0:
    n = float(input())
    if 0 <= n <= 10:
        n2 = n
    else:
        print("nota invalida")

media = (n1 + n2) / 2

print("media = {:.2f}".format(media))