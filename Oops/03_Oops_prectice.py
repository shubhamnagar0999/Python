
#1.
class Programmer:
    company = "Microsoft"
    def detail(self):
        print(f"The Id of Employee : {self.Id}\n The Age of Employee : {self.age}\n")

Shubham = Programmer()
Shubham.Id = "0999"
Shubham.age = 21
Shubham.detail()

Roshan = Programmer()
Roshan.Id = "0888"
Roshan.age = 21
Roshan.detail()

Poonam = Programmer()
Poonam.Id = "0777"
Poonam.age = 20
Poonam.detail()

#with parameters

class Programmer:
    company = "Microsoft"
    def detail(self,Id,age):
        print(f"The Id of Employee : {Id}\n The Age of Employee : {age}\n")

Shubham = Programmer()
Shubham.detail("0999",21)

Roshan = Programmer()
Roshan.detail("0888",21)

Poonam = Programmer()
Poonam.detail("0777",20)

#2.Calculator
#With method
class Calculator:
     
    @staticmethod
    def greet(n):
        print(f"hellow {n}")

    def squar(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num 
    
c = Calculator()
c.num = 2
c.greet("Shubham")
print(c.squar())
print(c.cube())

#with Constructor
print("With Constructor")
class Calculator:
    def __init__(self,num):
         print(num * num)
         print(num * num * num )

c = Calculator(3)

#3.
class a:
    a = 444
    def show(self):
        return self.a

b = a()
b.a =10000                           #if you will crate same name attribute that already class have the value of attribute will change 
print(b.show())

