'''trendy'''


u=int(input())
l=int(input())
for i in range(l,u):
    d=0
    m=1
    sum=0
    temp=i
    while temp>0:
        d=temp%10
        m=m*d
        sum+=d
        temp=temp//10
    res=sum+m
    if res==i:
        print(i)
        