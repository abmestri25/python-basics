# a = 10
# b = 3
# print(int.__add__(a,b))
# print(int.__mul__(a,b))
# print(int.__sub__(a,b))

# v = 'Abhishek '
# w = 'Mestri'

# print(str.__add__(v,w))

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>=s2:
            return True
        else:
            return False
    
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2) 

s1 = Student(34,43)
s2 = Student(43,34)
s3 = s1 + s2
print(s3.m1)

if s1>s2:
    print("S1 is greater")
else:
    print("S2 is greater")

print(s1)
print(s3)
print(s2)

