name = "kalu don"
Age = 21
print("The name is : ",name,"\n","The age is : ",Age)   

a = ("The name is : {} The age is : {}") 
b = a.format(name,Age)
print(b)

c = "The name is : %s the age is : %s"%(name,Age)
print(c)

print(f"The name is {name} The age is {Age}")