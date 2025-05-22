"""
Create a class called animal with a method
sound() that prints "Animal makes a sound."
Create a derived class called dog that inherits
from animal and overrides the sound()
method to print "Dog barks." Create another
derived class called bird that inherits from
animal and overrides the sound() method to
print "Birds sing".
"""

class animal():
    def sound(self):
        print("Animals makes sound")

class dog(animal):
    def sound(self):
        print("Dog Barks")

class bird(animal):
    def sound(self):
        print("Birds sing")


t1 = animal()
t1.sound()

t2 = dog()
t2.sound()

t3 = bird()
t3.sound()