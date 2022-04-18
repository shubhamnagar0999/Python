#epoch = is a point where the time start
import time
import datetime


print(time.time())  #it returns number of ticks(1 tick = 1 sec) from the time starts in python

print(time.ctime())  #it returns the current time

print(time.localtime(time.time()))  #it convert the second in to date and time and return an object
t = time.localtime(time.time())
print(f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}",t.tm_mday,t.tm_mon,t.tm_year)
