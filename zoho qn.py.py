'''given a array of numbers and a numbers k print the max possible k digit numbers which can
be form using given numbers

input:

4
1 4 973 97
3

output:

974

'''









import itertools as it 
n=int(input())
a=input().split()
b=int(input())
c=list()
for i in range(0,n+1):
    d=list(it.permutations(a,i))
    for j in d:
        f=""
        f=f.join(j)
        if(len(f)==b):
            c.append(f)
print(max(c))