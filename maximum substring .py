



a=input()
res=[a[i: j]for i in range(len(a))
        for j in range(i+1,len(a)+1)]
res.sort()

e=[]
for i in res:
    if i not in e:
        e.append(i)
print(e[-1])

