#Class variable types : class variable, Instance variable
class mobile:
    
    chargertype = "C-TYPE"  #class variable

    def __init__(self,model,price):
        self.model=model #Instance variable
        self.price=price #Instance variable

    def display(self):
        print("Model : ",self.model)
        print("Price : ",self.price)
        print("ChargerType : ",self.chargertype)

    
samsung = mobile("Samsung","20,000")
oppo = mobile("Oppo","10,000")

samsung.display()
oppo.display()
