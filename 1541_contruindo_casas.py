medidas = input().split(" ")

if str(medidas) == "['0']":
    a = 0
    b = 0
    c = 0
else:
    a, b, c = medidas

area = 0
ladoDelta = 0


while int(a) != 0 and int(b) != 0 and int(c) != 0:
    if 1 <= int(c) <= 100:
        area = int(a) * int(b)

        delta = (area*100)/int(c)
        episilon = (delta**.5)

        print(int(episilon))
        medidas = input().split(" ")

        if str(medidas) == "['0']":
            a = 0
            b = 0
            c = 0
        else:
            a, b, c = medidas