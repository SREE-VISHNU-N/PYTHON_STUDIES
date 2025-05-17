""" Get input for score out of 100.
    if score is <35 = "poor student"
    if score is greater than 35 but <than 70 = "Average student"
    if score is greater than 70 = "Good student" """


a = int(input("Enter your score : "))

if(a<35):
    print("poor student")

elif(a>=35 and a<70):
    print("Average student")

elif(a>70 and a<100):#You can stop in elif not must write else section
    print("Excellent student")

else: #Optional
    print("Enter below 101")