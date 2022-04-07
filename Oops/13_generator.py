"""

iterable : Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. ... For example,
            a list is iterable but a list is not an iterator.
iterator : an iterator is an object that enables a programmer to traverse a container,with function __next__() 


"""

name = "Mr.Stark"          #this is iterable you can use fuction iter()
it = iter(name)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# Generator is a fuction that does not return a single values it return a iterator object use yeild instead of return
def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
        yield f

g = fac(5)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)

def fib():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(10):
        c = a+b
        yield c
        # print(c)
        a = b
        b = c

d = fib()
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())

def fibrec(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1
    
    else:
        return fibrec(n-1)+fibrec(n-2)

print(fibrec(6))

#once the iteration is finish will not repreat again
S = " hellow sir my name is shubham"
L = iter(S)
print(L.__next__())
for i in L:
    print(i)  

for i in L:
    print(i)







