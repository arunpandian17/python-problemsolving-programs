a=input()
l=len(a)
if l%2!=0:
    m=(l//2)
    for i in range(1,l+1):
        if i==m-1 or i==m or i==m+1:
            print(a[i],end="")
else:
    print("invalid input")

'''
s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
m1=l1//2
m2=l2//2
for i in range(0,l1):
    if i==m1:
        print(s2,end="")
    else:
        print(s1[i],end="")
        
print()
'''
'''
s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
m1=l1//2
m2=l2//2

def pri(i):
    print(s1[i],end="")
    print(s2[i],end="")

def prit(s,i):
    print(s[i],end="")
    
if l1>l2:
    l=l1
else:
    l=l2

for i in range(0,l):
    if i==0:
        pri(i)    
    elif i==m1 :
        prit(s1,i)
    elif i==m2:
        prit(s2,i)
    elif i==l1-1 :
        prit(s1,i)
    elif i==l2-1:
        prit(s2,i)
'''
'''
s=input()
l=len(s)
for i in range(0,l):
    if ord(s[i])>=32 and ord(s[i])<=47:
        print("#",end="")
    else:
        print(s[i],end="")'''
        
'''        
s=input()
l=len(s)
v=0
sp=0
c=0
d=0

for i in range(0,l):
    if ord(s[i])==32:
        sp+=1
    elif ord(s[i])>=48 and ord(s[i])<=57:
        d+=1 
    elif s[i]=='a' or s[i]=="A" or s[i]=="e" or s[i]=="E" or s[i]=="i" or s[i]=="I" or s[i]=="o" or s[i]=="O" or s[i]=="u" or s[i]=="U" :
        v+=1
    else:
        c+=1
print("vowels:",v,"space:",sp,"con:",c,"digit:",d)        '''

'''
s1=input()
s2=input() 
print(s1.count(s2)) 
'''

'''s=input()
f=input()
l=len(s)
c=0
for i in range(0,l):
    if s[i]==f:
        c=i
print(c+1)
'''
'''
s=input()
l=[]
for i in range(0,len(s)):
    if ord(s[i])>=97 and ord(s[i])<=122:
        print(s[i],end="")
    else:
        l.append(s[i])
for i in range(0,len(l)):
    print(l[i],end="")
    '''
      

