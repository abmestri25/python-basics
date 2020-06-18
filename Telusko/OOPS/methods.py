# There are three types of methods 
# Instance   self       none
# Class      cls        @classmethod 
# Static     none       @staticmethod 

# Instance Method
# It is concern only with instance variable
class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_marks(self):
        return self.m1,self.m2,self.m3
        
# object
s1 = Student(35,34,12)

print("This is average",s1.avg())
print("These are the marks of student 1:",s1.get_marks())


# Class Method
# It is concern only with class variable
class Student:
    # class variable
    school = "Telukso"

    @classmethod
    def get_school(cls):
        return cls.school

print("This is the name of school",Student.get_school())

# Static Method
# when we are not concern about class varaible and instance variable that time we use it
class Student:

    @staticmethod
    def info():
        print("This is static method statement")

Student.info()



        