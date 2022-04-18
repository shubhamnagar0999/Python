#without args
# def people(a,b,c,d):
#     print(a,b,c,b)

#no need to create parameter of each argument.
#if you want to pass a parameter with args you will specifiy parameter first in function

def people1(n,*p):
    print(n)
    for i in p:
        print(i)

peo=("shubham","Roshan","Poonam","Hariom")
people1("Pooja",*peo)

