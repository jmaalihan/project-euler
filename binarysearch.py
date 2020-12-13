#naive search example

def naive_search(l, target):
	for i in range(len(l)):
		if l[i]==target:
			return i
		return -1

#given a sorted list and a target value in that list, return the index of the target value

def binary_search(l,target,low=None, high=None):
	if low is None:
		low=0
	if high is None:
		high= len(l)-1

	if high < low:
		return -1

	midpoint= (high+low)//2
	if l[midpoint]==target:
		return midpoint
	elif l[midpoint]>target:
		return binary_search(l,target, low, midpoint-1)
	else:
		return binary_search(l,target,midpoint+1, high)



print(binary_search([1,2,3,33,40,50], 33))