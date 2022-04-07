class Prime:
    prime = 1
    def primeNumber(self,nth):
        for i in range(2,nth):
            check = nth%i
            if check==0:
                self.prime=0
    
        if self.prime==1:
            print("This is a prime Number.")
        else:
            print("This is not a prime Number.")


p = Prime()
num = int(input("Enter The Number To check Number is Prime : "))
p.primeNumber(num)