'''
given an array of positive integers print the number which have longest continous range



INPUT:

5
1 3  10 7  9 2 4 6


OUTPUT:

1234

'''

n=int(input())
a1,res=[],[]
a=list(map(int,input().split()))
a.sort()
while len(a)!=0:
    
        #print(a,a1)
        m=min(a)
        
        if m+1 in a:
            a1.append(m)
            a.remove(m)
            
        else:
            a1.append(m)
            a.remove(m)
            res.append(a1)
            a1=[]
mx=0        
res.sort()
for i in res:
    if mx<len(i):
        mx=len(i)
for i in res:
    if mx==len(i):
        print(*i)
