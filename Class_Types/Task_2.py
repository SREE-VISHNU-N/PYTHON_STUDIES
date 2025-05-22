#Types of methods

class phone():
    chargertype = "B-TYPE"

    def __init__(self):
        self.price = 20
        self.model = ""

    def setprice(self,price): #Instance funtion
        self.price = price
        print(self.price)
    
    @classmethod #Class function
    def charger(cls):
        cls.chargertype = "C-TYPE"
        print(cls.chargertype)

    @staticmethod #Static function
    def static():
        print("This is static method")


mob = phone()
mob.setprice(20000) #Instance function or method
mob.charger()
phone.charger() #Class function or method
mob.static() # Static funtion or method
        
