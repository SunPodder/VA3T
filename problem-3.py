input = input(">> ").lower()
reversed = input[ : :-1]

if input == reversed:
	print("YES")
else:
	print("NO")