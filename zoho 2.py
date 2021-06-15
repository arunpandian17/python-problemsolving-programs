'''
given two sorted array of distinct elements there is only 1 diff between the array first array has one elements
extra added in between find the index of extra elements


input:
N=7
a[]={2,4,6,8,9,10,12}
b[]={2,4,6,8,10,12}
output:
4

'''
#answer:

import numpy as np 
a=np.fromstring(input(), dtype=int, sep=',')
b=np.fromstring(input(), dtype=int, sep=',')
for i in range(len(a)):
    if a[i] not in b:
        print(i)
        break