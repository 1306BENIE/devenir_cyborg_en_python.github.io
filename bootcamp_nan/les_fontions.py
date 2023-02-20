def function_fibonacci(n):
	a = 1
	b = 1
	output = []
	for number in range(n):
		output.append(a)
		a, b = b, a+b

	return output


for x in function_fibonacci(10):
	print(x)