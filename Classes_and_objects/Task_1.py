#Example of class function 


class goa:
    name = ""
    drink = ""

    def party(self):
        print("Lets party......")

    def beach(self):
        print("Enjoying beach")


ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh kumar"
suresh.name = "Suresh kumar"

ramesh.drink = "Yes"
suresh.drink = "No"

print(ramesh.name)
print("Drink : ",ramesh.drink)
ramesh.party()

print("")

print(suresh.name)
print("Drink : ",suresh.drink)
suresh.beach()


