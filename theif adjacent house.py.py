
a=list(map(int,input().split()))
s=a[0]
c=0
while sum(a)>0:
    c+=s
    for i in range(0,len(a)):
        if s==a[i]:
            a[i]=0
            if i-1 != -1:
                a[i-1]=0
            if i+1<len(a):
                a[i+1]=0
    s=max(a)
print(c)
    
    
    
    