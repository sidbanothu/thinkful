## Fibonacci 


# def Fibonacci(a,b):
	# print("Adding {0} & {1} = {2}".format(a,b, a+b))
	# c = a + b
	# return Fibonacci (b,c)
	
# Fibonacci(0,1)

def Fibonacci(n):
	if n < 2:
		return n
	else:
		return Fibonacci(n-2) + Fibonacci(n-1)

answer = Fibonacci(10)
print answer