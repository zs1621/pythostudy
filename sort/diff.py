import random
import json
import merge_sort
import maopao
import time
import radix_sort
A = []
B = []
C = []
jon = []
#ran = 9000000000000000000000000000000000000000000000000000000000000000000
ran = 2 ** 140
length = [1000, 10000, 30000, 50000]
for lent in length:
    for i in range(0,lent):
        num = random.randint(100000,ran)
        A.append(num)
        #B.append(num)
        C.append(num)

    start2 = time.clock()
    radix_sort.radixsort(C)
    radix_time = time.clock() - start2
    print ("tong use time: ", time.clock() - start2)


    start = time.clock()
    merge_sort.sort(A, 0, len(A))
    merge_time = time.clock() - start
    print ("merge sort use: ", time.clock() - start )
    jon.append({"x": lent, "mst": merge_time, "rst": radix_time})

f = open('result.json','w')

f.write(json.dumps(jon))

#start1 = time.clock()
#maopao.mp(B)
#print ("maopao use time:", time.clock() - start1)
