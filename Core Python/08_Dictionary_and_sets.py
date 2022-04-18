#Dictionary
#you can not inset duplicate keys
#it is unorderd

Dic = {
    "Shubham" : "Mr.Stark",
    "Hariom"  : "Yadav",
    "Roshan"  : "Jha",
     "Age"  : [21,21,22],
     4:5,
     "first" : {"second":"third"}     #
}


   

print(Dic["Shubham"],"\n",Dic["Hariom"])
print(Dic[4])
print(Dic["first"]["second"])

#Functions
print(Dic.items())    #this will written all key and values
print(Dic.keys())     #will print only keys

print(Dic.update({"Shubham":"kalu"}))#will update value of keys
print(Dic)

print(Dic.get("shubham"))       #if key not present this will return noneand direct method shows error

#Sets
#set has not repetative elements

Set = {3,4,5,6,7,7,3}  #repetative elements will not print
print(Set)
print(type(Set))

#for create empty set
se = set()
print(type(se))

#repetative elments will not print.
se.add(3)
se.add(3)
se.add(44)
se.add(34)
se.add(35)
se.add(34)
se.add(345)
print(se)

 #function on sets
print(len(se))   #retrun length of set

se.remove(345)          
print(se)       #remove 345 from the list1

se.pop()         #remove any element from the list
print(se)

#se.clear()       #will clear the set
#print(se)

see=se.union({345,46,77,88,99,35}) #this will retrun all elments from both set
print (see)

seee =se.intersection({3,44})
print(seee)                       #only those elments that are presents on both sets


#Prectice

Diction = {
     "bhagna" : "Run",
     "khana"  : "eat",
     "Rona"   :  "Cry"
}
print(Diction["bhagna"])
print(Diction.keys())

#2.
# num1 = int(input("Enter 1 Number : "))
# num2 = int(input("Enter 2 Number : "))
# num3 = int(input("Enter 3 Number : "))
# num4 = int(input("Enter 4 Number : "))
# num5 = int(input("Enter 5 Number : "))
# num6 = int(input("Enter 6 Number : "))
# num7 = int(input("Enter 7 Number : "))
# num8 = int(input("Enter 8 Number : "))

# dis = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(dis)

#3.
ForCheck ={1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,
           
         "a","b","c","d",          
         "e","f","g","h",
         "i","j","k","l",
         "m","n","o","p",
}                                   #this can be done also
print(ForCheck)

#4.

h = set()
h.add(20)
h.add(20.0)
h.add("20")

print(len(h))

#5.
d = {

}
print (type(d))

#6.
Friend = {

}
Friend.update({"Shubham":"Java",
                "Roshan":"html",
                "Tushar":"html",
                "Shubham":"Python"
})#if name repeate the values of previous name will update
print(Friend)