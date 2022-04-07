#List

a = [3,4,5,2,1,3,4,6,7,77,55,33,22]  #like array
a[0]=1000
print(a)

#Functions of list
a.sort()
print(a)                             #function will arrange in ascending order.
#a.reverse()
#print(a)                             #decending order

a.append(333)                        #this will add 333 at last of the list
print(a)

a.insert(3,44)                        #inset 44 at index 3
print(a)

a.pop(3)
print(a)                              #will delete provided index

a.remove(55)
print(a)


#tuple are imutable

b = (3,4,6,4,3,6645,433,3)
print (b)
#b = ()  empty tuple
#if you want to make tuple with one value you need to provide (,) after the value
d = (3,)

#b[1]=4                               can't change value 
print(b)
#function of tuple

b.count(3)                           # return occurence of 3
print(3)                               

print(b.index(6645))                 #index number


#Prectice 
#1.
Fruite = input("Enter 1 fruite.")
Fruite1 = input("Enter 2 fruite.")
Fruite2= input("Enter 3 fruite.")
Fruite3 = input("Enter 4 fruite.")
Fruite4 = input("Enter 5 fruite.")
Fruite5 = input("Enter 6 fruite.")
Fruite6 = input("Enter 7 fruite.")

fruits_list = [Fruite1,Fruite2,Fruite3,Fruite4,Fruite5,Fruite6,Fruite]
print(fruits_list)

#2.
marks1 = input("Marks of 1 student.")
marks2 = input("Marks of 2 student.")
marks3 = input("Marks of 3 student.")
marks4 = input("Marks of 4 student.")
marks5 = input("Marks of 5 student.")
marks6 = input("Marks of 6 student.")

MarksList = [marks1,marks2,marks3,marks4,marks5,marks6]
MarksList.sort()
print(MarksList)

#3.
num = (7,0,8,0,0,9)
print(num.count(0))