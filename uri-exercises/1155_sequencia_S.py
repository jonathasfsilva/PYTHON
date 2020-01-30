s = 1
for x in range(100):
    s = s + (1/(x+1))
print("{:.2f}".format(s-1))