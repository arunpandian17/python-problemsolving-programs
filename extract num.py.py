'''a=input()
sum=0
res=0
a=int(a)
while int(a)>0:
    b=int(a)%10
    sum+=b
    a//=10
while sum>0:
    sum1=sum%10
    res+=sum1
    sum//=10
print(res)


'''
a=4
c=(a<<3)-a
print(c)