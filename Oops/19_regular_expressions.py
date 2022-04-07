'''
Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string


'''
# fuction in regular expressions (findall , search , split , sub , finditer)
import re
code = '''
iterable : Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. ... For example,
            a list is iterable but a list is not an iterator.
iterator : an iterator is an object that enables a programmer to traverse a container,with function __next__() 


"""

name = "Mr.Stark"          #this is iterable you can use fuction iter()
it = iter(name)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# Generator is a fuction that does not return a single values it return a iterator object use yeild instead of return
def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
        yield f

g = fac(5)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)

def fib():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(10):
        c = a+b
        yield c
        # print(c)
        a = b
        b = c

d = fib()
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())

def fibrec(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1
    
    else:
        return fibrec(n-1)+fibrec(n-2)

print(fibrec(6))

#once the iteration is finish will not repreat again
S = " hellow sir my name is shubham"
L = iter(S)
print(L.__next__())
for i in L:
    print(i)@  

for i in L:
    print(i)
919773406368

kaludon hai 
kaludon hai 
kaludon hai 
kaludon hai 
'''
# print(re.findall("kaludon hai",code))     #this will print number of specific pattern in code

# print(re.search("i", code))

# print(re.split("@", code))                  #will split you string in to part from your provided pattern

# print(re.sub("hai", "kalu", code))

#we use raw string in re

s = re.compile(r" ^i")
si = s.finditer(code)
for i in si:
    print(i)

import re
s = '''hll how are you can you do something for me i need a help how 919773602997

'''
a = re.compile(r"91\d{10}")
A = a.finditer(s)
for i in A:
    print(i)