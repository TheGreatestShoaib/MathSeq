import math


inp = int(input("k :"))


def xibonacci(x):
	inp = int(x)
	emp = []
	for i in range(inp-1):
		emp.append(0)
	emp.append(1)
	while True:
		x = emp[-inp:]
		emp = emp[-inp:]
		y = sum(emp)
		yield emp[-1]
		emp.append(y)


hello = xibonacci(inp)

for _ in range(100):
	print(next(hello))