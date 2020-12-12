def fib(n):
	if n<=0: 
		return
	elif n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)



def compute():
	x=1
	evenFibList=[]
	while fib(x)<4000000:
		if fib(x)%2==0:
			evenFibList.append(fib(x))
		x+=1
	return sum(evenFibList)



print(compute())