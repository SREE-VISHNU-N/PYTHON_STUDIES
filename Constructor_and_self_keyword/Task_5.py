"""
Create a class called calculator
Create 2 varibles a and b
Create a function called add,sub,mul,div all functions
should take 2 variables as parameter
Pass the a and b value through object().

"""

class calculator:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2

    def add(self):
        print("Sum :",self.num1+self.num2)

    def sub(self):
        print("Difference :",self.num1-self.num2)

    def mul(self):
        print("Product :",self.num1*self.num2)

    def div(self):
        print("Quotient :",self.num1/self.num2)
        print("Remainder :",self.num1%self.num2)
        

a = int(input("Enter a : "))
b = int(input("Enter b : "))
op = input("| + | - | * | / | : ")

a_and_b = calculator(a,b)

if(op == "+"):
    a_and_b.add()

if(op == "-"):
    a_and_b.sub()

if(op == "*"):
    a_and_b.mul()

if(op == "/"):
    a_and_b.div()    #Hureyyy ha ha ha ha, easy but for me hard........mmm
