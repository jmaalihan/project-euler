def isPrime(n):
	return all(n%i!=0 for i in range(2,n))

def nthPrime(n):
	x=2
	primeList=[]
	while len(primeList)<n:
		if isPrime(x):
			primeList.append(x)
		x+=1
	return(primeList[-1])

print(nthPrime(10001))

#104743