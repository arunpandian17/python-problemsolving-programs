'''
A company has decided to give some gifts to all of its employees.for that the company has given some
rank to the employees.based on the rank company has distributed the gifts.
rules:
1)each employee must receive atleast one gifts
2)employees having higher ranking get a greater number of gifts
3)what is the minimum number of gifts requires by company



INPUT:
2
5
12152
2 
12 

OUTPUT:
7
3


'''



n=int(input())
for i in range(n):
    a=int(input())
    a1=list(map(int,input().split()))[:a]
    c=0
    for j in range(len(a1)):
        if (l[i]<l[i-1]):
            c+=1 
        else:
            c+=2
    print(c)
