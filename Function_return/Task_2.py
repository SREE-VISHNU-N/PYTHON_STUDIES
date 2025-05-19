"""Get input for a and b and function called add()
   which should return sum of a and b and multiply the 
   sum with c"""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

def add(n1,n2): # or any other variable
    add = n1+n2
    return add

sum = add(a,b)
mul = sum*c

print (mul)