class Person:

    # Class Variable
    type = "Human"

    #Instance Variables
    def __init__(self):
        # Varaibles
        self.name = "Abhi"
        self.age = 21

    def update(self):
        self.name = "Premdas"
    
    def compare(self,other):
        if first.name == other.name:
            return True
        else:
            return False

# Objects
first = Person()
second = Person()

second.update()

if first.compare(second):
    print("They are same")
else:
    print("They are not same")

print(first.name,first.type)
print(second.name)

        


