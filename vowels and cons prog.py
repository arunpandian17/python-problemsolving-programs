s="lead the team".split()
x=""
v=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(s)):
    for j in range(len(s[i])-1):
        if s[i][j] in v and s[i][j+1] in v:
            x=x+s[i]
print(x,end="")
