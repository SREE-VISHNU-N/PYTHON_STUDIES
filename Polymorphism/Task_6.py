"""
Create a base called employee with
properties name and salary. Create a derived
class called manager that inherits from 
employee and adds a property department.
Write a method in manager to display the
name, salary, and department of the manager.

"""

class employee():
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary


class manager(employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)   
        self.department = department

    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        print("Department : ",self.department)


t1 = manager("vishnu","1,00,000","Electronics")
t1.display()


