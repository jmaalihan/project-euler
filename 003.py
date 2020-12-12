#compute returns the largest prime factor of n

def isPrime(n):
	return all(n%i!=0 for i in range(2,n))

def factorList(n):
	return [x for x in range(1,n) if n%x==0]

def compute(n):
	return max([x for x in factorList(n) if isPrime(x)])
	

print(compute(21))

