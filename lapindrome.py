
'''develop a program for lapindrome
in='xyz''zyx'
in='abckbca'''



def odd():
    s=a[0:m]
    d=a[m+1:l]
    for i in s:
        if i in d:
            print("y")
        else:
            print("n")
def even():
    s=a[0:m]
    d=a[m:l]
    for i in s:
        if i in d:
            print("y")
        else:
            print("n")



a='abckcba'
l=len(a)
m=l//2
if m%2!=0:
    odd()
else:
    even()