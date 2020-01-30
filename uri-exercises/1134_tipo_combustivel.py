t = 1
alcool = 0
gasolina = 0
diesel = 0
while t != 4:
    t = int(input())

    if t == 1:
        alcool = alcool + 1
    elif t == 2:
        gasolina = gasolina + 1
    elif t == 3:
        diesel = diesel + 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))