#def is a keyword that mean it is a fuction
def add(a):
    return a[0]+a[1]+a[2]+a[3]

c = [3,4,4,3]
print(add(c))

#default parameter function
def gre(b="Good one"):
    print("hellow ",b)

b1 = input("what is your name\n")
gre()

#recursion
def rec(val):
    if val==0 or val ==1:
        return 1
    else:
        return val * rec(val-1)

value = int(input("enter number to ger the factorial."))
print(rec(value))

#iterative
def rec1(val):
    n = 1
    for i in range(1,val+1):
        n = n * i 
    print(n)

value = int(input("enter number to ger the factorial."))
rec1(value)

#docString if you want to write somethinge in about what your fuction do you can write in (__doc__)string
def sum(a,a1):
    """you can't add three of more than three number"""
    print(a+a1)
print(sum.__doc__)   #this will print your doc string
sum(3,5)

'''
#prectice
#1.
def greater(num,num1,num2):
    if num>num1:
        num3 = num
    else:
        num3 = num1

    if num3>num2:
        print(num3," is greater ")
    else:
        print(num2," is greater ")

num1 = int(input("enter the 1 number :"))
num2 = int(input("enter the 2 number :"))
num3 = int(input("enter the 3 number :"))
greater(num1,num2,num3)


#2.
def celcius(c):
    return (c*9/5)+32

celcius1 = int(input("Enter celcius : "))
value = celcius(celcius1)
print(value," F")

#3.
def sun_n(number):
    if number ==1:
        return 1
    else:
        return (number) + sun_n(number-1)

print(sun_n(10))

#4.
def pat():
    n=5
    for i in range (n):
        print("* "*(n*1-i))

pat()

#5.
def inch(i):
    return i/0.39

print(inch(1))'''