n = []
x = float(input())
n.append(x)
for i in range(99):
    x = x/2
    n.append(float(x))
    print("N[{}] = {:.4f}".format(i, n[i]))
print("N[{}] = {:.4f}".format(99, n[99]))