pedido = input().split(" ")

cod, qtd = pedido

if int(cod) == 1:
    print("Total: R$ {:.2f}".format(4*int(qtd)))
elif int(cod) == 2:
    print("Total: R$ {:.2f}".format(4.5 * int(qtd)))
elif int(cod) == 3:
    print("Total: R$ {:.2f}".format(5 * int(qtd)))
elif int(cod) == 4:
    print("Total: R$ {:.2f}".format(2 * int(qtd)))
elif int(cod) == 5:
    print("Total: R$ {:.2f}".format(1.5 * int(qtd)))