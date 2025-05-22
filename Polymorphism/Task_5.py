"""
Create a base class called vehicle with a
method start() that prints "Vehicle started"
Create a derived class called car that inherits
from vehicle an overrids the start()
method to print "Car started"

"""

class vehicle():
    def start(self):
        print("Vehicle started")

class car(vehicle):
    def start(self):
        print("Car started")


t1 = car()
t1.start()