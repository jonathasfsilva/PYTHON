qtd = int(input())
soma = 0
x = 1

if 1 <= qtd <= 20:
    for i in range(qtd):
        n = int(input())
        if 1 <= n <= (10**8):
            while x <= (n / 2):
                if n % x == 0:
                    soma = soma + x
                x = x + 1

            if soma == n:
                print("{} eh perfeito".format(n))
            else:
                print("{} nao eh perfeito".format(n))

            x = 1
            soma = 0