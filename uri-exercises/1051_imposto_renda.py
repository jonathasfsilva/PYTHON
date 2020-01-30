renda = float(input())

if 0 < renda <= 2000:
    print("Isento")
elif renda <= 3000:
    resto = renda - 2000
    imposto = resto * 0.08
    print("R$ {:.2f}" .format(imposto))
elif renda < 4500:
    resto = renda - 3000
    imposto = (resto * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(imposto))
else:
    resto = renda - 4500
    imposto = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(imposto))