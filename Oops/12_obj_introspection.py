o = "hellow"
# print(type(o))   #show the type of the variable
# print(id(o))      #every varible has a uniqe id you  can see with this function
# print(dir(o))      #it provide of method for o 

import inspect 
print(inspect.getmembers(o)) 
