qtd = int(input())
div = 0
x = 1

if 1 <= qtd <= 100:
    for i in range(qtd):
        n = int(input())

        if 1 <= n < (10**7):
            while x <= n / 2:
                if n % x == 0:
                    div = div + 1
                x = x + 1
            div = div + 1

            if div == 2:
                print("{} eh primo".format(n))
            else:
                print("{} nao eh primo".format(n))

            div = 0
            x = 1