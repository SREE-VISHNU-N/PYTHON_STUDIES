""" Get input for salary and age.
    If salary greater than or equal to 20000 or age less than or equal to 25,
    get input for required loan amount. if not print you are not eligible for loan.
      
    if loan amount is less than or equal to 50000 print you are eligible for loan.
    if greater than 50000 print maximum loan amount is 50000  """



salary = int(input("Enter your salary : "))
age = int(input("Enter your age : "))

if(salary>=20000 or age<=25):
    
    loan = int(input("Required loan amount : "))
    if(loan<=50000):
        print("You are eligible for loan")

    else:
        print("Maximun loan amount is 50000")

else:
    print("You are not eligible for loan")