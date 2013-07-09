
#author github @zs1621
def sort(A, a, b): 
	n = b - a
	begin = a	
	end = b
	if (b + a) % 2 == 0:
		middle = (b + a) / 2
	else:
		middle = (b + a + 1) / 2 
	if n <= 1:
		print "arr len < 2"
		return A
	elif  n == 2 :
		merge(A, begin, middle, end)
	else:
		if middle - begin > 1:
			sort(A, begin, middle)
		if end - middle > 1:
			sort(A, middle, end)
		merge(A, begin, middle, end)
			
	
def merge(A, a, b, c):
	B = range(0,c)  
	i = a 
	j  = b 
	total = c - a
	k = 0
	while i < b and j < c:
		if A[i] < A[j]:
			B[k] = A[i]
			i += 1
			k += 1
		else:
			B[k] = A[j]
			j += 1	
			k += 1
	if i == b:
		while j < c:
			B[k] = A[j]
			k += 1
			j += 1
	if j == c:
		while i < b:
			B[k] = A[i]
			k += 1
			i += 1
	k = a
	for i in range(0, total):
		A[k] = B[i]	
		k += 1
		i += 1
	
if __name__ == "__main__":
	start = time.clock()
	sort(A, 0, len(A))
	print ("merge sort use: ", time.clock() - start )
