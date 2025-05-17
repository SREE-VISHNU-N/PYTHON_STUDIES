"""  Get input for variable income. If income is greater than 7000
     scholarship is available. Else not eligible for scholarship  """


income = int(input("Enter your income : "))

if(income<=7000):
    print("You are eligible for scolarship")

else:
    print("You are not eligible for scolarship")
