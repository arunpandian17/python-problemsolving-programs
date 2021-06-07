'''In a Conference ,attendees are invited for a dinner after the conference.The Co-ordinator,Sagar arranged around round tables for dinner and want to have an impactful seating experience for the attendees.Before finalizing the seating arrangement,he wants to analyze all the possible arrangements.These are R round tables and N attendees.In case where N is an exact multiple of R,the number of attendees must be exactly N//R,,If N is not an exact multiple of R, then the distribution of attendees must be as equal as possible.Please refer to the example section before for better understanding.
For example, R = 2 and N = 3
All possible seating arrangements are
(1,2) & (3)
(1,3) & (2)
(2,3) & (1)
Attendees are numbered from 1 to N.

Input Format:

The first line contains T denoting the number of test cases.
Each test case contains two space separated integers R and N, Where R denotes the number of round tables and N denotes the number of attendees.
Output Format:

Single Integer S denoting the number of possible unique


Constraints:

0 <= R <= 10(Integer)
0 < N <= 20 (Integer)
Sample Input 1:
1
2 5
Sample Output 1:
10
'''
#ANSWER:






from itertools import combinations
n=int(input())
for m in range(0,n):
    inp=input().split()
    a=int(inp[0])
    b=int(inp[1])
    #print(a)
    #print(b)
c=0
l=[]
for i in range(1,b+1):
    l.append(i)
ce=combinations(l,b//2+1)
for i in list(ce):
    c+=1
    #print(i)
print(c)
        
        
        