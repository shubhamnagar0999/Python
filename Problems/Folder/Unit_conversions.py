class UnitConversins:
    @staticmethod
    def kms_miles(km):
        miles = km * 0.621
        return miles

    @staticmethod
    def inchs_feet(inch):
        feet = inch * 0.0833
        return feet
        
    @staticmethod
    def cm_inch(cm):
        inch = cm * 0.394
        return inch

    @staticmethod
    def pound_kgs(pound):
        kg = pound * 0.454
        return kg

    @staticmethod
    def inches_meter(inch):
        meter = inch * 0.0254
        return meter

if __name__ == '__main__':
    UC = UnitConversins()
    print("\n1. Enter A To Convert km to Miles.")
    print("2. Enter B To Convert inches to feet.")
    print("3. Enter C To Convert cm to inchs.")
    print("4. Enter D To Convert pound to kgs.")
    print("5. Enter E To Convert inches to meter. ")
    print("6. Enter Q To Quit. \n")

    for i in range(10):


        choice = input("Please Enter Your Choice : \n")
        if choice == 'A' or choice == 'a' :
            try:
                km = float(input("\nEnter Kms to Convert In Miles : "))
                miles = UC.kms_miles(km)
                print(f'{miles} Miles in {km} KM.\n')
            except Exception as e:
                print("Enter Valid Option.")

        elif choice == 'B' or choice == 'b':
            try:
                inch = float(input("\nEnter inches to Convert In feet : "))
                feet = UC.inchs_feet(inch)
                print(f'{feet} Feets in {inch} inches.\n')
            except Exception as e:
                print("Enter Valid Option.")

        elif choice  ==  'C' or choice == 'c':
            try:
                cm = float(input("\nEnter cm to Convert In inchs : "))
                inches = UC.cm_inch(cm)
                print(f'{inches} Inches in {cm} cms.\n')
            except Exception as e:
                print("Enter Valid Option.")

        elif choice  ==  'D' or choice == 'd':
            try:
                pound = float(input("\nEnter Pound to Convert In kgs : "))
                kgs =  UC.pound_kgs(pound)
                print(f'{kgs} kgd in {pound} Pound.\n')
            except Exception as e:
                print("Enter Valid Option.")
    
        elif choice  ==  'E' or choice == 'e':
            try:
                inches = float(input("\nEnter Inches to Convert In Meters : "))
                meter = UC.inches_meter(inches)
                print(f'{meter} Meters in {inches} Inches.\n')
            except Exception as e:
                print("Enter Valid Option.")

        elif choice  ==  'Q' or choice == 'q':
            break

        else:
            print('Invalid Choice.\n')
    