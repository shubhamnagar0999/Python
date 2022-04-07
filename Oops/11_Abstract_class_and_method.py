# from abc import ABC,abstractmethod
#class Base(ABC):
from abc import ABCMeta,abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def mul(self,a,b):
        return 0

class Child(Base):
    def add(self):
        print("hellow")

    def mul(self,a,b):
        self.a = a
        self.b = b
        return self.a*self.b

class Child2(Child):
    @staticmethod
    def do():
        print("hy")
    
c = Child2()
print(c.mul(3,4))
