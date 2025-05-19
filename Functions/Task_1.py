#Simple calculator using def funtion 


def add():
    add=a+b
    print("Sum is : ",add)

def sub():
    sub=a-b
    print("Difference is : ",sub)

def mul():
    mul=a*b
    print("Product is : ",mul)

def div():
    div=a/b
    print("Quotient is : ",div)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

op=input("| + | - | * | / | : ")

if(op=="+"):
    add()

if(op=="-"):
    sub()

if(op=="*"):
    mul()

if(op=="/"):
    div()
    
    