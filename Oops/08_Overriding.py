#if a method or constructor is override there is no existance of previous one without (super())
class A:
    line = "hellow i am class A"
    time = "i will take less than both"
    def __init__(self):
        self.line = "hellow i am contructor of A class"
        # self.time = " i will take 50 sec "
        # self.time = "I will take 20 sec"
        

class B(A):
    time = " i will take less than A"
    def __init__(self):
        super().__init__()  
        # self.time = " i will take 30 sec"                           
        self.line = "hellow i am contructor of B class"   #after override prvious instance will no longer exits
        pass                                                 # if you want to use that you can use it with super()
                                                         #if you write super first it will run constructor of parent class first
                                                         #if you write super first it will run constructor of parent class later
     
fa = B()
print(fa.line)
print(fa.time)                                            #it will find in class B constructor if constructor have "time instance variable" than
                                                          #it will print if not than it will check parent class construtor if you provided "super()"
                                                          #if not than it will check "class B time vairable" if class b have than it will print if not 
                                                          #than it will check "class A time varible
