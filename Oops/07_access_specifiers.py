class A:
    value = 10        #public 
    _value2 = 11      #protected 
    __value3 = 12     #private 

class B(A):
    value4 = 33

b = B()
print(b.value)       #public can use form its child 
print(b._value2)     #protected can use form its child class

a = A()
print(a._A__value3)  #python use name mangling to save it for access the value3 you will acees with (_class name)




