import time
def mp(A):
    len1 = len(A)
    len2 = len(A)
    for j in range(0,len1):
        for i in range(0,len2):
            if i+1 < len2:
                if A[i] >= A[i+1]:
                    temp = A[i]
                    A[i] = A[i+1]
                    A[i+1] = temp
        len2 -= 1
if __name__ == "__main__":
    start = start.clock()
    mp(A)
    print ("maopao use time:", time.clock() - start)
