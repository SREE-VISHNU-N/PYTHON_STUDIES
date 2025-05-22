"""
Create a class called teacher
Create a varibale - name and register number using constructor
Create a function called display which should display the name and
register number of the teacher
Create t1 and t2 object and pass the name and reg no value through
object

"""

class teacher:
    def __init__(self,n,r):
        self.name = n
        self.register = r
    def display(self):
        print("Name : ",self.name)
        print( "Register number : ",self.register)

t1 = teacher("vishnu","12345")
t2 = teacher("sree","54321")

t1.display()
t2.display()