x = int(input())
y = int(input())

while x < y:
    i = x + 1
    if (i % 5 == 2 or i % 5 == 3) and (i != y):
        print(i)
    x = x + 1

while y < x:
    i = y + 1
    if (i % 5 == 2 or i % 5 == 3) and (i != x):
        print(i)
    y = y + 1