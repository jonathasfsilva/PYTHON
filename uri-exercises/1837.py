#a = b × q + r

linha = input().split()

a, b = linha

q = int(a)/int(b)
q = int(q)
r = int(a)%int(b)


if int(a) < 0 and int(b) < 0:
	q = int(a) /int(b)
	q = int(q)
	if q * int(b) + (int(a)%int(b)) != int(a):
		q = q + 1
	r = int(a) % int(b)
	while int(q) * int(b) + (int(a)%int(b)) != int(a):
		r = r + 1
		print("aaaa")

elif int(b) < 0:
	while int(a) != int(b) * q + r:
		q = int(a) / int(b)
		q = int(q)
		r = r + 1
elif int(a) < 0:
	q = int(a) / int(b)
	q = int(q) - 1
	while int(a) != int(b) * q + r:
		r = r + 1	

print(q,r)