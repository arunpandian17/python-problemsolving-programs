a=input()
z=a.split()
n=len(z)
r=[]
for i in range(0,n):
    for j in range(i+1,int(n)):
        if(z[i]==z[j]):
            r.append(z[j])+
for i in r:
    print(i)
