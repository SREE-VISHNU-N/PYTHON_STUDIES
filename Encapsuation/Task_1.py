"""
class company():
    def __init__(self):
        self.__CompanyName = "Google" #private variable __used.


    def companyname(self):
        print(self.__CompanyName)


t1 = company()
t1.companyname() """


class company():
    def __init__(self):
        self._CompanyName="Google" #It is protected varible

class companyname(company): #You can access from inheritance method
    pass

t1 = companyname()
print(t1._CompanyName)