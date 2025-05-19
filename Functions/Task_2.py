#def function method two
"""
def vishnu(msg):
    print("The message is : ",msg)

vishnu("Hello world")

"""

#Get a integer number from user and pass it to the function
#Let the funtion print whether the number is even or odd


def even_or_odd(find):
    if(find%2 == 0):
        print("The given number is Even")

    if(find%2 != 0):
        print("The given number is Odd")


num = int(input("Enter a number : "))

even_or_odd(num)
