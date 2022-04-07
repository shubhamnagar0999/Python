class Father:
    a = 29
    b = 33

    def __init__(self,num):
        self.num = num

    def __truediv__(self,self1):
        return self.num + self1.num


    def __str__(self):                              #in this dunder method you can write what your class work
        return "For Dunder Methods"

    def __repr__(self):                             #in between "__str__ and __repr__" this will call str 
        return f"{self.a} + {self.b}"
        
F = Father(20)
F2 = Father(22)
print(F / F2)
# print(sm)

# print(F)                                            #in between "__str__ and __repr__" this will call str if str not present 
                                                    #than it will call "__repr__"

# print(repr(F))                                      #if you want to call "__repr__" 


