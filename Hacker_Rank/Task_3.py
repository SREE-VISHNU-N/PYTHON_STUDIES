n = int(input())

n1 = n*3
n2 = n*5
if(n1%3 == 0 and n2%5 == 0):
    print("FizzBuzz")

elif(n1%3 == 0 and n2%5 != 1):
    print("Fizz")   #Not finished yet