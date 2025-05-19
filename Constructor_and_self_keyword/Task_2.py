"""
Create a class called student
Create a variable - name and register number using constructor
Create a function called display which should display the name and
register number of the student.
"""

class student:
    def __init__(self):
        self.name = ""
        self.register_number = ""

    def display(self):
        print("Name : ",self.name)
        print("Resister number : ",self.register_number)


details = student()


details.name = input("Enter name : ")
details.register_number = int(input("Enter reister : "))

details.display()