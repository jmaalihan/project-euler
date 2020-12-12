def evenDiv(x,n):
	return all(x%i==0 for i in range(1,n+1))

def compute():
	x=2520
	while True:
		if evenDiv(x,20):
			return x
		x+=1
	

print(compute())
