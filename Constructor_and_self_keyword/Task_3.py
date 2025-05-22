"""
Create a class called fruit
Create a variable called colour using __init__ method
Create a object called apple "Pass the color variable as
a parameter through object"
"""
class fruit:
    def __init__(self,col):
        self.colour=col
        


apple = fruit("red")

print(apple.colour)