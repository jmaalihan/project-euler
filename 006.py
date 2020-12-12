def sumSquares(n):
	return sum(x**2 for x in range(1,n+1))

def squareSums(n):
	return sum(x for x in range(1,n+1))**2

def compute():
	return squareSums(100)-sumSquares(100)

print(compute())
#returns 25164150