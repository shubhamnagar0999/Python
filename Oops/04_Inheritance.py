'''#single inheritence
class A:
    @staticmethod
    def add(a,b):
        return a+b

class a(A):
    @staticmethod
    def mul(a,b):
        return a*b

obj = a()
print(obj.add(4,34))
print(obj.mul(4,34))

#multiple inheritance
class Roshan:
    def speak(self):
        print("i am web developer")

class Hariom:
    def tell(self):
        print("I am android developer")

    def speak(self):
        print("web and android")            

#when method is override in second class the method will run of the class that is gave first as argument in the child class
#this conditon will also applied for class attribute

class shubham(Hariom,Roshan):       #the first class as argument has max priority than second class as argument
    def telling(self):
        print("I can do both")
      
emp = shubham()
emp.speak()

# multilevel inheritence
class company:
    name = "amazon"
    def give(self):
        print("give work to the manager")

    def work(self):
            print("i gave")

class manager(company):
    name = "Shubham"
    def take(self):
        print("handle work and give to employes")

    def work(self):
        super().work()  #if you want to use upper class method also which have same name
        #you can use it for constructor as(super().__init__())
        print("i take then gave to the employe")

#if method is overirde then this will print nearest method

class employe1(manager):
    def do(self):
        print("done work")

e = employe1()
e.work()

#@classmethods

class year:
    year = 2021
    month = 20
    day = "3 mon"

    # def change(self,y):
    #     self.year = y            #this will not change class attribute will make an instance attribute
    
    # def change(self,y):
    #     self.__class__.year = y    #with this you can change class attribute

    #with @classmethod
    @classmethod
    def change(cls,y):
        cls.year = y

obj = year()
print(obj.year)
obj.change(2020)
print(obj.year)
print(year.year)

# exercise

class c2d:
    def d(self,i,j):
        self.i = i
        self.j = j

        return f"{self.i}i + {self.j}j"

class c3d(c2d):
    def d3(self,i,j,k):
        # super().d(i,j)
        self.k = k
        return f"{self.i}i + {self.j}j + {self.k}k"

# d = c2d()
# print(d.d(2,3))
    
d2 = c3d()
print(d2.d(3,5))
print(d2.d3(3,4,5))

#2.

class Animal:
    pass

class pet(Animal):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("bhauu..... bhau......")

d = dog()        
d.bark()
'''
#3.
class Employee:
    addsalary = 10000
    increment = 3000
    
    @property
    def inc(self):
        return self.addsalary + self.increment

    @inc.setter
    def inc(self,v):
        self.increment = v - self.addsalary

e = Employee()
print(e.inc)
e.inc = 11500
print(e.increment)

#4.
