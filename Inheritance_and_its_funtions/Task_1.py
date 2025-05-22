"""
INHERITANCE
If one class can access another class is called single heritance
If one cass can access multiple calss is called multiple heritance


class dad():
    def phone(self):
        print("Dad's phone")

class mom():
    def sweet(self):
        print("Mom's sweet")

class son(mom,dad): #single, and multipe
    def laptop(self):
        print("Son's laptop")


vishnu = son()
vishnu.laptop()
vishnu.sweet()
vishnu.phone()

"""

#Multi level Heritance

class grandpa():
    def phone(self):
        print("Grandpa's phone")

class dad(grandpa):
    def money(self):
        print("Dad's money")

class son(dad):
    def laptop(self):
        print("Son's laptop")


vishnu = son()
vishnu.laptop()
vishnu.money()

d1 = dad()
d1.money()
d1.phone()


"""Hiararchial inheritance - if mutiple classes based on any one class is called,
Hiararchial inheritance (eg: We have four classes lika father, son1, son2, son3. 
if three sons can access father class) 

Hybrid - if all those methods can used in one program called Hybrid.(eg: 
we have four 5 classes lika father , land, son1, son2, son3. In this method 
three sons can access father calss, and son1 can access father class and land class.)

"""