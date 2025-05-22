"""
The word polymorphism means having many forms. In programmingm, polymorphism
means the same function name (but different signature) being used for different
types. The key difference is the data types and number of arguments used in function.

"""

#For example

def add(a,b,c=0):
    print(a+b+c)

add(30,10)
add(10,20,30)