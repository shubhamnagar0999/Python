import time
from functools import lru_cache

@lru_cache(maxsize=2)
def sum(a):
    n = 0
    time.sleep(3)       #it  will sleep the loop for 3 sec
    for i in range(a):
        n = n + i
    return n

print(sum(3))           #this will save in cache and if you call again will not take 3 sec
print(sum(4))
print(sum(3))
print(sum(4))

