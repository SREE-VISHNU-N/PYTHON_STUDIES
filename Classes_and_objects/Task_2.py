"""
Create a class called laptop and create a following
variables and functions:
variables - price, processor, ram
create object - HP, DELL, LENOVO  and print it

"""



class laptop:
    price = ""
    processor = ""
    ram = ""

HP = laptop()
DELL = laptop()
LENOVO = laptop()

HP.price = "30,000"
HP.processor = "13th Gen Intel Core i3"
HP.ram = "8GB "

DELL.price = "40,000"
DELL.processor = "AMD Ryzen 5 5500U"
DELL.ram = "8GB"

LENOVO.price = '45,000'
LENOVO.processor = "AMD Ryzen 5 7520U"
LENOVO.ram = "8GB"

print("FOR HP")
print("Price : ",HP.price)
print("Processor : ",HP.processor)
print("Ram : ",HP.ram)
print("")

print("For DELL")
print("Price : ",DELL.price)
print("Processor : ",DELL.processor)
print("Ram : ",DELL.ram)
print("")

print("For LENOVO")
print("Price : ",LENOVO.price)
print("Processor : ",LENOVO.processor)
print("Ram : ",LENOVO.ram)