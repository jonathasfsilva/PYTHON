linha = input().split()

a, b = linha

q = int(a) / int(b)
r = abs(int(b) * int(q) - int(a))

if int(a) < 0 and int(b) < 0:
    q = int(a) / int(b)
    q = int(q) + 1


print(int(q),int(r))