#Comprehensions : offer a shorter syntax

#--> 1. List Comprehension <--

#with out list comprehension
l = []
for i in range(100):
    l.append(i)
print(l)

#with list comprehension
l2 = [i for i in range(100)]
print(l2)

#--> 2. Dic. Comprehension <--

dic = {i:f"Student {i}" for i in range(10)}
print(dic)
print(type(dic))

dic2 = {value:key for key,value in dic.items()} #dic reveser
print(dic2)

#--> set Comprehension <--

Set = {i for i in [1,1,2,3,4,4,5]}
print(Set)
