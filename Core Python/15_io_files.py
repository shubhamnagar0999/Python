#there are two type of file
#text files
#binary files

#open take two parameters one is path of txt file and second is mode type
#by default the mood is r if we don't provide mood
fil = open("C:\\Users\\Mr.Stark\\Downloads\\1.txt","r")
print(fil.read())
#print(fil.read(3))                 #will read only three charecters of file
print("the index is ",fil.tell())   #this will tell the index
print(fil.seek(3))                  #set index
print(fil.readline())               #this will read first line 
#print(fil.readline())              #read 2nd line
fil.close()

#write mood
fil2 = open("C:\\Users\\Mr.Stark\\Downloads\\1.txt","w")
print(fil2.write("good boy\n"))    #this will write text in your text file
print(fil2.write("hellow bro"))
fil.close()

#append mood
fil3 = open("C:\\Users\\Mr.Stark\\Downloads\\1.txt","a")
fil3.write("done bro")             #this will add to the file
fil3.close()

#(with statement) with this statement no need to close file
with open("C:\\Users\\Mr.Stark\\Downloads\\1.txt","r") as fil4: 
    print(fil4.read())

with open("poem.txt","w") as poems:#write will automaticaly create file
    poems.write('hlo')
