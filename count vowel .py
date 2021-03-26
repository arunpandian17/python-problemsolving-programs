'''str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0
spaces=0
number=0
str1.lower()

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    elif i>='0' and i<='9':
        number=number+1
    elif(i==" "):
        spaces=spaces+1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
print("Total numbers",number)
print("Total  number of spaces",spaces)
'''

