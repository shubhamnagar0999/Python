class library:
    def __init__(self,lis,name):
        self.lis = lis
        self.name = name
        self.dic = {}
    
    def display_book(self):
        print(f"Books are avilable in library {self.name}")
        for Book in self.lis:
            print(Book)

    def lend_book(self,book,user):
   
        if book not in self.dic.keys():
            self.dic.update({book : user})
        else:
            print(f"the book is taken by {self.dic[book]}")
           
        # print(self.dic.items())
        # self.lis.remove(book)
      
        
    def add_book(self,book):
        self.lis.append(book)

    def retrun_book(self,book):
        self.dic.pop(book)
        
if __name__ == '__main__':
    lis = ["java","html","css","c#","c++","python"]
    L = library(lis,"Programming")
    
    while(True):
        print("\nEnter Your Choice : ")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book\n")

        In = int(input())

        if In == 1:
            L.display_book()

        elif In == 2:
            book = input("Enter book name : ")
            user = input("Enter your name : ")
            L.lend_book(book,user)
       

        elif In == 3:
            foradd = input("enter book for add")
            L.add_book(foradd)

        elif In ==4:
            addreturn = input("Enter the book to return")
            L.retrun_book(addreturn)
        else:
            print("invalied choice")

        print("Enter q for quit and c for ")
        In2 = input()
        if In2 is "q":
            exit()
        elif In2 is "c":
            continue

        