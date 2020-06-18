class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop('Lenovo','i5','8GB')
    
    def show(self):
        print(self.name,self.rollno ,end=" ") 
        self.lap.showinfo()

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        
        def showinfo(self):
            print(self.brand,self.cpu,self.ram,) 
    
s1 = Student('Abhishek',25)
s2 = Student("Shaurya",23)

s1.lap.brand = "Apple"

s1.show()
s2.show()
