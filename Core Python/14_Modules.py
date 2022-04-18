# import random                           #this module used for generate random num.
# r = random.randint(1,10)
# print(r)

#time module

import time

ini = time.time() #time is a fuction in time module that gives number of ticks(1 tick = 1 sec)
print(ini)
for l in range(1000):
    print("Hey")
print(time.time()-ini)
l = 0

ini1 = time.time()
while(l<1000):
    print("kalu")
    time.sleep(2)  #this will print kalu int every 2 sec
    l +=1
print(time.time()-ini1)


Time = time.asctime(time.localtime(time.time()))
print(Time)