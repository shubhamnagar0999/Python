year = int(input('Enter The Year To Check Leap Year : '))
if year%4==0 and year%100!=0 or year%400==0:
    print("The Year is Leap Year.")
else:
    print("This Year is Not a leap Year.")
    