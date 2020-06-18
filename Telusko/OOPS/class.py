# Class is blueprint of object in OOPS
# From classes we can create objects

class Computer:
    def config(self):
        print("i5,1TB SSD,16GB")

# Object is created
comp = Computer()  

# This is precesural way to access method
Computer.config(comp)

# This is most preffered way to access method
# Accessing the configuration of object comp
comp.config()     