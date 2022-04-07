#if you wnat to make a fuction and use it as property


class time:
    fixtime = 8
    extratime = 4

    @property          #now this will work like property you can use it
    def totletime(self):
        return self.fixtime  + self.extratime  

    @totletime.setter
    def totletime(self,v):
       self.extratime = v - self.fixtime 

t = time()
print(t.totletime)
t.totletime = 10

print(t.totletime)
print(t.extratime)

# a = t.min+60
# print(a)             #you can use value as property now




