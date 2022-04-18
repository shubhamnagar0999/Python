#Must remember
'''a=45
if(a>3):
    print("greater")           #you have to provide one spaces or one tab after conditon
else:                          #the else condition is touch to the exect left side
    print("both")

#if else ladder.
if(a<10):
    print("a is greater than 10")
elif(a<15):
    print("a is greater than 15")
elif(a<20):
    print("a is greater than 20")
elif(a<30):
    print("a is greater than 30")
else:
    print("Done")

#multiple if statement
if(a==10):
    print("a is equal to 10")
if(a<10):
    print("a is greater than 11")
if(a<15):
    print(" a is greater than 15")
else:
    print("done")

#is and in
b = 2
if(b is 22 or b is 2):
    print("yes")
else:
    print("no")

c =[3,4,3,2,3]
print(33 in c)

#prectice
#1.
num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
num3 = int(input("Enter 3 number: "))
num4 = int(input("Enter 4 number: "))

if(num1 > num2 and num1>num3 and num1 > num4):
    print(num1 ," is greater" )
elif(num2 >num1 and num2 > num3 and num2 >num4):
    print(num2, " is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3,"is grater")
else:
    print(num4," is grater")

#2.
Physics = float(input("Enter the marks of physics : "))
Maths = float(input("Enter the marks of Maths : "))
Chemistry = float(input("Enter the marks of Chemistry : "))

average = (Physics+Maths+Chemistry)/300
per = average*100
print(per)
if(Physics>33 and Maths>33 and Chemistry>33 and per>=40):
    print("Congratulation You passed")
else:
    print("Sorry you are fail")


#4.
Username = input("Enter the Name : ")
length = len(Username)
print(length)
if(length>10):
    print("the length of Username is greater than 10")
else:
    print("the length of Username is less than 10")
'''
#5.
record = ("Tushar","Roshan","kaptaan","shubham")
Name = input("Enter the name")
if(Name in record):
    print("Name is present")
else:
    print("Not present")


