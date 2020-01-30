sal = float(input())

if 0 <= sal <= 400:
    newSal = sal * 1.15
    reaj = newSal - sal
    print("Novo salario: {:.2f}".format(newSal))
    print("Reajuste ganho: {:.2f}".format(reaj))
    print("Em percentual: 15 %")
elif 400 < sal <= 800:
    newSal = sal * 1.12
    reaj = newSal - sal
    print("Novo salario: {:.2f}".format(newSal))
    print("Reajuste ganho: {:.2f}".format(reaj))
    print("Em percentual: 12 %")
elif 800 < sal <= 1200:
    newSal = sal * 1.1
    reaj = newSal - sal
    print("Novo salario: {:.2f}".format(newSal))
    print("Reajuste ganho: {:.2f}".format(reaj))
    print("Em percentual: 10 %")
elif 1200 < sal <= 2000:
    newSal = sal * 1.07
    reaj = newSal - sal
    print("Novo salario: {:.2f}".format(newSal))
    print("Reajuste ganho: {:.2f}".format(reaj))
    print("Em percentual: 7 %")
elif 2000 < sal:
    newSal = sal * 1.04
    reaj = newSal - sal
    print("Novo salario: {:.2f}".format(newSal))
    print("Reajuste ganho: {:.2f}".format(reaj))
    print("Em percentual: 4 %")