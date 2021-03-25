'''armstrong number'''
def arms(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

        if num == sum:
            print(num,"is an Armstrong number")
        else:
            print(num,"is not an Armstrong number")
   
   
start=int(input())
end=int(input())
num = int(input("Enter a number: "))
 
if num>start and num<end:
    arms(num)
else:
    print("valid input please.....")