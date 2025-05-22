"""
Create a base class called shape with a method
area() that returns 0. Create a derived class 
called rectangle that inherits from shape
and overrides the area() method to calculate
and return the area of a rectangle.

"""

class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self,l,v):
        rec = l*v
        return rec
       
    

call = rectangle()
print(call.area(11,7))
    

