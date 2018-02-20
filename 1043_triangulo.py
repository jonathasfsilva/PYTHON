linha = input().split(" ")

a, b, c = linha

if abs(float(b) - float(c)) < float(a) < float(b) + float(c):
    per = float(a) + float(b) + float(c)
    print("Perimetro = {:.1f}".format(per))
elif abs(float(a) - float(c)) < float(b) < float(a) + float(c):
    per = float(a) + float(b) + float(c)
    print("Perimetro = {:.1f}".format(per))
elif abs(float(a) - float(b)) < float(c) < float(a) + float(b):
    per = float(a) + float(b) + float(c)
    print("Perimetro = {:.1f}".format(per))
else:
    area = ((float(a)+float(b))*float(c))/2
    print("Area = {:.1f}".format(area))