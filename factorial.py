


'''Factorial'''


def facti(low,upp):
    fact=1
    for i in range(upp,low-1,-1):
        fact=i*fact
    print(fact)

low=int(input())
upp=int(input())
if low >0 and upp>0:
    facti(low,upp)
elif low==0 or upp==0:
    print("0")
    
else:
    print("please enter valid number")


