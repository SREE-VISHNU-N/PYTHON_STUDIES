try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)


except ValueError as e:
    print("ValueError",e)
except Exception as e:
    print("Something wrong",e)

finally:
    print("Done")

