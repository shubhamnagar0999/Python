from array import array


arr = array('i',[3,4,3,2,3,4,5,2,1]) #first takes typecode and second takes values
print(arr.typecode)                  #gives element type of array
print(arr.buffer_info())             #gives memory location and number of values in array
print(arr.append(88))

for i in arr:
    print(i)