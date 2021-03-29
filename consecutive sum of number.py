#a,a+1,a+2,.....a+n-1
#(a+a+n-1)*n/2=N
#a=naturl num (+ve)
#a=(2N n-n**2)/2n---formula(it should be positive)






def sol(N):
    c=0
    n=2
    while 2*N +n - n**2>0:
        a=(2*N   + n  - n**2)/(2*n)
        if a - int(a) == 0:
           
            c+=1
        n+=1
    return c
    
    
    
#N=int(input())
print(sol(int(input())))



