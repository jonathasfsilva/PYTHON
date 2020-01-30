n = int(input())
x = 1
while x <= n/2:
    if n % x == 0:
        print(x)
    x = x + 1
print(n)