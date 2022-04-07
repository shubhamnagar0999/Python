class Poject:
    Collage_Name="AITM"

    def __init__(self,Name):             #no need to call constructor
        print("Hellow How are you",Name)

    def chat(self):
        print(f"Autho Id : {self.Id}")
        print("I can send or recive sms.")
     
    @staticmethod          
    def call():
        print("i can call.")

Shubham = Poject("Mr.Stark")  