import random
import merge_sort
import maopao
import time
import radix_sort 
A = []
B = [] 
C = []
ran = 9000000000000000000000000000000000000000000000000000000000000000000
ran = 2 ** 140
length = 20000
for i in range(0,length):
	num = random.randint(100000,ran)
	A.append(num)
	#B.append(num)
	C.append(num)

start2 = time.clock()
radix_sort.radixsort(C)
print ("tong use time: ", time.clock() - start2)


start = time.clock()
merge_sort.sort(A, 0, len(A))
print ("merge sort use: ", time.clock() - start )

#start1 = time.clock()
#maopao.mp(B)
#print ("maopao use time:", time.clock() - start1)


