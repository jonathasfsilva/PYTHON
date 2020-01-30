par = 0
imp = 0
pos = 0
neg = 0

for x in range(5):
    aux = int(input())

    if aux % 2 == 0:
        par = par + 1
    if aux % 2 == 1:
        imp = imp + 1
    if aux > 0:
        pos = pos + 1
    if aux < 0:
        neg = neg + 1

print("{:.0f} valor(es) par(es)".format(par))
print("{:.0f} valor(es) impar(es)".format(imp))
print("{:.0f} valor(es) positivo(s)".format(pos))
print("{:.0f} valor(es) negativo(s)".format(neg))