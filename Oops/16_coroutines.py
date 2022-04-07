import time
def read():
    time.sleep(2)
    R = "hellow don i can fuck you any time any where"
    
    while True:
        ser = (yield)
        if ser in R:
            print("yes")
        else:
            print("no")

r = read()
next(r)         #to start this you use next method on the instance 
r.send("i")
r.send("hellow")
r.send("kaly")
r.send("don")



    