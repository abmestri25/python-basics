class A:
    def __init__(self):
        print("In init of A")
    def feature(self):
        print("This is feature of class A")

class B(A):
    def __init__(self):
        # This is used to get features from superclass
        super().__init__()
        print("In init of B")
    
    def feature(self):
        print("This is feature of class B")

    
