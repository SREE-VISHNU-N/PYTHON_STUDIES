class a():
    def __init__(self):
        print("A")
    def display():
        print("This is from A")


class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display():
        print("This is from B")


class c(b):
    def __init__(self):
        super().__init__()
        print("C")
    def display():
        print("This is from C")



op = c()





