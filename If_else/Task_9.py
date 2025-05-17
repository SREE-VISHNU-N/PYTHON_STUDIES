""" Get input for five subjects marks. Add all of it, and find average.
    if average mark is less than 35, print "Additional class is required"
    else print "You are good to go"  """


T = int(input("Tamil : "))
E = int(input("English : "))
M = int(input("Maths : "))
S = int(input("Science : "))
SS = int(input("Social Science : "))

sum = T+E+M+S+SS
avg = sum/5

if(avg<=35):
    print("Average : ", avg)
    print("Additional class is required")

else:
    print("Average : ", avg)
    print("You are good to go")