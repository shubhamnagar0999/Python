Name = 'Shubham'    #can write in double and triple quote also
Name2 = '''k
a
l
u'''                 #Triple quote use when want to print more than one line.
print(Name)

#String Slicing.
#each alphabet has a perticular index in string.

line = "hellow i am shubham nagar i can do calisthanics.\n"
print(line[7])       #will type 'i' that present on index.
print(line[0:19])    #will print from start to shubham.

#can also print from last with 
#Negetive Indices

print(line[-10:-1])   #will start from last.

#Slicing with skip values.
print(line[0::2])     #this will skip every second alphabet of string.

#String Functions.

print(len(line))     
print(line.count("a"))
print(line.endswith("s."))
print(line.capitalize())
print(line.find("shubham"))
print(line.replace("shubham","Roshan"))

#prectice
#1.
Input = input("Enter Your name.")
print(Input,"Good Afternoon")

#2.
a = '''Dear Shubham
             ypu are selected
             5\\7\\54'''
print(a)
    

#3
line = "hellow  i  am  shub  ham  na  gar  i  do calisthanics.\n"
print(line.find("  "))
print(line.replace("  "," "))