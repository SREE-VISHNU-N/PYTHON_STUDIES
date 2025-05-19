class laptop:
    def __init__(self):
        self.ram = ""
        self.processor = ""

    def display(self):
        print("Ram : ", self.ram)
        print("Processor : ",self.processor)


hp = laptop()

hp.ram = "8GB"
hp.processor = "AMD Ryzen 5"

hp.display()