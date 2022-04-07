'''#while loop
a =1
while a<=50:
    print(a)
    a = a+1


friends = ['roshan','hariom','poonam','lakshmi']
b=0
while b<len(friends):  
    print(friends[b])
    b = b +1

# for loop

friends = ['roshan','hariom','poonam','lakshmi']
for c in friends:
    print(c)

#range fuction

for a in range(50):    #from 1 to 50 only last end
    print(a)

for a in range(30,50):    #from 30 to 50 start and last end
    print(a)

for a in range(30,50,2):    #from 30 to 50 start and last end and every second element will skip
    print(a)
else:
    print("finish")          #else can be use with for and while

#break and contineous
a=1
for a in range(15):
    print(a)
    if a==10:
     break
     
else:                        #else will print when the loop succesfully finish
    print("done")


for a in range(1,15):
    if a==10: 
        continue              #this will skip 10 and than continue
    print(a) 

#prectice
table = int(input("Enter the number to get the table."))
num=1
for num in range(1,11):
    num = table*num
    print(num)

#2.
List = ["Harry","shubham","sachin","roshan"]
for a in List:
    if a.startswith("s"):
        print("Hellow ",a)

#
n = int(input("Enter the number to get the Factorial."))
fact = 1
while (n>=2):
    fact = fact*n
    n-=1
print(fact)

n = int(input("Enter the number to get the Factorial."))
fac =1
for i in range(1,n+1):
    fac = fac * i

print(fac)
'''
#3
j=4
for i in range(4):
    print (" "*(j-i),end="")
    print("*"*(2*i+1),end="")    
    print(" "*(j-1))
   