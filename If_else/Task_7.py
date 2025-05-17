""" Get a input for score percentage. Only if the percentage is greater
    than 70,  get input for his name, department and location. Then
    print you are eligible. If not print you are not eligible  """


score = int(input("Enter your score : "))

if(score>=70):
    print("You are eligible")

    name = input("Enter your name : ")
    department = input("Enter your Department : ")
    location = input("Enter your location : ")

    print("Name : ",name)
    print("Department : ",department)
    print("Location : ",location)


else:
    print("You are not eligible")