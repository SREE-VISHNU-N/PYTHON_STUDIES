""" Get a input for a and b and pass it to the function,
    let the function print the range of a and b. """


def printrange(first,second):
    for i in range(first,second):
        print(i)

a = int(input("Enter a : "))
b = int(input("Enter b : "))

printrange(a,b)