#when you use multiple inheritance and also method overriding it create confusion
# that which class method will be considered 
class A:
    @staticmethod
    def dance():
        print("I can write somethinge i am class A")
 
class B(A):
    @staticmethod
    def dance():
        print("I can write somethinge i am class B")
 
    
class C(A):
    @staticmethod
    def dance():
        print("I can write somethinge i am class C")
 
class D(B,C):
    @staticmethod
    def dance():
        print("I can write somethinge i am class D")
 


d = D()
d.dance()      #will go first with "class D" if it have "dance()" than print if not than go to 
               #it parent class if "class B and Class C" one of than has "dance()" fuction than will print if not than 
               #check class B and class c parent class 