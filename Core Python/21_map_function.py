l = [3,4,5,6,5,4]
# l = int(l[3])+1
# print(l)

#with loop
# for i in l:
#     i = 5 + int(i)
    # print(i)
    
#with map function
# print(list(map(int,l)))  #it take two arguments one function that you want to apply and second on which you want to apply
def s(n):
    return n*2

a = list(map(s,l))
print(a)

#with lambda function
# a = list(map(lambda n:n*2,l))
# print(a)

#also have filter and reduce function same as map
#from functools import reduce

#filter function

def s1(n):
    return n>2

a = list(filter(s1,l))               #the map fuction will return true in this situation
print(a)

#reduce function
from functools import reduce
l1 = [4,5,6,7,8]

a = reduce(lambda x,y:x+y,l1)
print(a)
