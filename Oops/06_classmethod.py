
class my:
    
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
        # print(f"the name is {self.name}")
        # print(f"the name is {self.age}")
        # print(f"the name is {self.id}")
    
    @classmethod
    def agee(cls,s) :
        cls.age = s
        print(f"the age is {cls.age}")

    def sername():
        return f"the sername is nagar"

    @classmethod                    #first advantage of class method is that it can use as altenative constructor
                                    #you can change value of class varible 
    def do(cls,s):
        # lawdu = s.split(".")
        # print(lawdu)
        return cls(*s.split("."))   #one line code with varargs

shubham = my("kalu",22,"02")
Roshan = my.do("roshan.23.01")
print(Roshan.name)
print(Roshan.id)

# shubham.agee(44)
# my.agee(shubham)


