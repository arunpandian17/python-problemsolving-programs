def fib(n):
    a, b = 0, 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1
       
       
       
       
n= int(input("terms :"))
if n>1:
    fib(n)
else:
    print("Enter valid number")
    
    