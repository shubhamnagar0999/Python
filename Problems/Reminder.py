import playsound 
import time
import multiprocessing
print(__name__)

def do():
    print("Sir time for drink water")
    playsound.playsound("P:\\My music\\2.mp3")
    print("done")

def take():
    a = input("Enter your name")
    print(a)

p1 = multiprocessing.Process(target=do)
p2 = multiprocessing.Process(target=take)

if __name__ == '__main__':
    
    p1.start()
    p2.start()