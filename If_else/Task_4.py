"""  Get input for a number and check whether it is divisible by both 
     3 and 5. If yes print, the number is divisible by 3 and 5 else 
    print the number is not divisible by 3 and 5.  """



a = int(input("Enter number : "))
"""
if(a%3 == 0):
    
        if(a%5 == 0):
              print("This number is divisible by 3 and 5")
        else:
               print("This number is divisible by 3 but not 5")

else:
       print("This number is not divisible by 3 and 5")

"""

if(a%3 == 0 and a%5 == 0):
    print("This number is divisible by 3 and 5")

else:
    print("This number is not divisible by 3 and 5")