from math import sqrt

linha = input().split(" ")
a, b, c = linha

delt = float(b)**2 - 4*float(a)*float(c)

if (2*float(a)) != 0 and delt >= 0:
    r1 = (-float(b) + sqrt(float(delt)))/(2*float(a))
    r2 = (-float(b) - sqrt(float(delt)))/(2*float(a))
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")