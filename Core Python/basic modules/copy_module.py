# deep copy : in deep copy any change made to a copy of object do not reflect in the orignal object.
# shallow copy : in case of shallow copy, reference of object point to copy in to the variable that means change will reflect to the orignal object. 
from copy import copy,deepcopy

#deep copy
l = [2,3,4,5,4,3,66]
print(l)

newl = deepcopy(l)
newl[0] = 100
# print(newl)
# print(l)

#shallow copy : normal list
newl2 = l.copy()   
newl2[0]=1111     #will point to the new location in memory
print(newl2)
print(l)

# shallow copy in nested list
l1 = [[1,2,3,4],[5,6,7,8]]
l2 = l1.copy()

l1[0][0] = 100
print(l1)
print(l2)

