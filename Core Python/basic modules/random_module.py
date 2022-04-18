import random

print(random.randint(1,10))  #this will return random number form 0 to 10

print(random.randrange(10))  #this will return random number between 0,10 except 0,10

print(random.random())  #this will return floating value between 0 and 1

print(random.uniform(11,20))  #this will return floating value between given number include starting number not last

l = [22,64,78,88,93,23,45,77]
print(random.choice(l)) # will return random number from given sequence. sequence can be list tuple or string

print(l)
random.shuffle(l)
print(l)