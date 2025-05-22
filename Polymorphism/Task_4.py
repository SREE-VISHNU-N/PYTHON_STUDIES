"""
Create a base class called person with a 
constructor that takes a name as a parameter.
Create a derived class called student that 
inherits from person and has a constructor
that takes a parameter called grade. Write a
method in student to display the name and 
grade of the student by using super keyword

"""

class person():
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print(self.name, self.grade)


t1 = student("Vishnu","A")
t1.display()



    


        