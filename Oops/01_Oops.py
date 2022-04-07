class cal:
    def add(self):
        print(f"sum of {self.a} and {self.b} is {self.a + self.b}")

class cal2:
    def mul(self):
        print(f"sum of {self.a} and {self.b} is {self.a * self.b}")
        
    
c = cal()
c.a = 13
c.b = 12
c.add()

m = cal2()
m.a = 5
m.b = 4
m.mul()

class Employe:
    company = "Microsoft"        #class attribute
    age = 21
    

Roshan = Employe()
#Roshan.age = 20                  #instance attribute
Shubham = Employe()
Shubham.age =20

#print(Roshan.company)          #this will print Microsoft
#change company name 
#Employe.company = "Google"

print(Roshan.company) 
print(Roshan.age)               #first it will check instance attribute if present than print otherwise check class attribure

print(Shubham.company)
print(Shubham.age) 

#self is a parameter that can use attributes of instance and class 
class Project:
    Collage_Name="AITM"
    def chat(self):
        print(f"Autho Id : {self.Id}")
        print("I can send or recive sms.")
     
    @staticmethod              #if you don't want to use fuction with out self.
    def call():
        print("i can call.")

Shubham = Poject()
Shubham.Id = "CS18022"
Shubham.chat() #this is equal to "Project.chat(Shubham)" thats why with self this will give error "chat() takes 0 positional arguments but 1 was given"

Roshan = Poject()
Roshan.Id = "CS18020"
Roshan.chat()
Roshan.call()

