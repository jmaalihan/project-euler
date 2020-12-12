def isPalindrome(n):
	nString=str(n)
	return nString==nString[::-1]

def compute():
	return max(i*j 
		for i in range(1,1000)
		for j in range(1,1000)
		if isPalindrome(i*j))
				

print(compute())
 
#906609
