import random
num = random.randint(1,100)

count = 1
for i in range(100):

    un = int(input("Enter a number: "))
    if num == un:
        print("Your chosse correct number in ",count,"guesses.\n")

        if count==1:
            print("Exilent Guess")
        elif count>1 or count<5:
            print("very good guess")
        else:
            print("good")
        break

    elif num>un:
        print("Your number is smaller.\n")
        count = count+1
    else:
        print("your number is grater\n")
        count = count+1