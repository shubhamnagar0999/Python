#try except are used for exception handling.

a = 4
b = 0
try:
    print(a/b)
except Exception as a:
    print("can't devide by zero")


#finally

try:
    num = int(input("Enter first number : "))
    num1 = int(input("Enter Second number : "))
    num3 = num * num1
    print(num3)

except Exception as e:
    print("Enter valied vlaue")

finally:
    mess = input("Enter you message")
    print(mess)
    print("this will run in any condition also if error occur")
    
try:
    L1 = open("poem.txt","r")
    L = open("Don.txt")


except Exception as e:
    print("does not exits")

finally:
    print(L1.read())
    L1.close()
    print("this will run in any condition also if error occur")

#else with try except
try:
    num = 3 * e
    print(num)

except Exception as e:
    print(e)

else:
    print("this will run only when except block will not run")
    