'''
Comprehensions in Python provide us with a short and concise way to construct 
new sequences (such as lists, set, dictionary etc.)

Python supports the following 4 types of comprehensions:
List Comprehensions.
Dictionary Comprehensions.
Set Comprehensions.
Generator Comprehensions
'''

#without list comprehensions
l = []
for i in range(100):
    if i%5==0:
        l.append(i)
# print(l)

#list comprehensions
l1 = [a for a in range(100) if a%5==0]
print(type(l1))
print(l1)

#dic comprehensions
dic = {key  : f"roll no {key} " for key in range(10)}
print(dic)
#you can also reverse dic with comprehensions
dic = {value:key for key,value in dic.items()}
print(type(dic))
print(dic)

#set comprehensions
# s = {}
# for i in range(3):
#     s.update({i:f"item{i}"})

# print(s)
s = {i for i in {"shubham","shubham","shubham","shubham","shubham","nagar","nagar"}}
print(type(s))
print(s)

#generator comprehensions
gen = (i for i in range(1,10))
print(gen)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
for i in gen:
    print(i)





