#it provides functions and variables to manipulate the python runtime environment.

import sys
print("hellow")

# sys.exit()         # for terminating program like for terminate loop we use break. for function we user return. 
print("kalu")

print(sys.path)      # variable prints path, where python modules are being searched
print(sys.platform)  #used for recognise host os system
print(sys.executable)#used to print executable python.exe file
# print(sys.modules)   #return modules list 

#important : sys.argv = for command line arguments
for i in sys.argv:
    print(i)





