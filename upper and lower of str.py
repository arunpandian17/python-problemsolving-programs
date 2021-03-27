#write a program to read astring and make the odd position chr in uppercase'''
#write a program to read a string and print consective vowels'''
#write a prog to read a string and display the word end with's'




s="america"
x=""
for i in range(0,len(s)):
    if i%2!=0:
        x=x+s[i].upper()
    else:
        x=x+s[i]
print(x)
    
