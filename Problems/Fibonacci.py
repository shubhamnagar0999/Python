#With iterative Approch
n = int(input("enter the number : "))
a = 0
b = 1
print(a,"\n",b)

for i in range (2,n+1):
    c = a+b
    a = b
    b = c 
    print( a+b)


#With recursive approch 
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(n))

