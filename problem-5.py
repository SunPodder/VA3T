def fib(n):
    l=[]
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
        print(''.join(str(li) for li in l))

while True:
	row = int(input("\n>> "))
	fib(row)
