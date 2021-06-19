'''
Find the least prime number  that can be added with first array element makes these divisible
by second array elemets at the respective index if exist return -1 as answer and consider
1 as prime number



INPUT:
[20,7]
[11,5]

OUTPUT:

13


'''






a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,1000):
    count=0 
    if i >1:
        for j  in range(2,i):
            if j%i==0:
                break
            else:
                for k in range(0,len(a)):
                    if (a[k]+i)%b[k]==0:
                        count+=1
                    else:
                        count=0 
            if count==len(a):
                print(i)
                break
            

