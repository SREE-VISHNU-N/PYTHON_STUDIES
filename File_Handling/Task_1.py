f = open("Fruits.txt","a")
f.write("apple\n")
f.write("supotta\n")
f.close

f = open("Fruits.txt","r+")
print(f.read(),"\n")

"""
File hanling modes,
a - append - for add new values with previous value
w - write - for add new values but it will remove all previous values
r - read - for read values in terminals

procedure:
open-->change current mode-->read or write-->close
"""
