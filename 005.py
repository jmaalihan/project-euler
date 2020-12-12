#brute force from 11-20, since factors 1-10 are included to avoid redundancy

def evenDiv(x,n):
	return all(x%i==0 for i in range(11,n+1))

def compute():
	x=1
	while True:
		if evenDiv(x,20):
			return x
		x+=1
	

#print(compute())

#alternative using prime factorization

#need pfd() that decomposes into prime factors

#for x in primeFactorList, count occurences in each :

def isPrime(n):
	return all(n%i!=0 for i in range(2,n))

def factorList(n):
	return [x for x in range(1,n) if n%x==0]






