"""
Set s_username = "vishnu" , s_password = "528528"

Get input for username and password from user

create a function called validate

if the username and password matches the function should
return true else false.

"""
""" It is my code, its correct but different

def validate(u,p):
    if(u == s_username and p == s_password):
        return "True"
    else:
        return "false"

username = input("Enter your username : ")
password = input("Enter your password : ")

s_username = "vishnu"
s_password = "528528"

a = validate(username,password)
print(a) """

def validate():
    if(username == s_username and password == s_password):
        return True
    else:
        return False

s_username = "vishnu"
s_password = "528528"

username = input("Enter your username : ")
password = input("Enter your password : ")

a = validate()
print(a)

