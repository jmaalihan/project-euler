def isPrime(n):
	return all(n%i!=0 for i in range(2,n))

def primesBelow(n):
	x=3
	primeList=[2]
	while True:
		x+=1
		if x==n:
			break
		if isPrime(x):
			primeList.append(x)
	return(primeList)


def compute(n):
	return(sum(primesBelow(n)))

print(compute(100))

#using small argument to test, compile time long

