""" Get a integer number from user and pass it to the funtion
if the number is greater than 35 print "You are pass"
if the number is less than 35 print "You are fail" """


def mark(value):
    if(value>=35 and value<=100):
        print("You are pass")

    elif(value<35):
        print("You are fail")


a = int(input("Enter your mark : "))
mark(a)