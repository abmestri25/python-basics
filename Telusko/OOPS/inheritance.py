# Inheriting features from parent class to child class or superclass to subclass
# It has three types
# Single Level Inheritance
# Multi Level Inheritance
# Multiple Inheritance

# Single Level Inheritance
# class B is able to use features from class A
class A:
    def feature1(self):
        print("This is feature 1")

class B(A):
    def feature2(self):
        print("This is feature 2")

a1 = A()
b1 = B()

# Multi Level Inheritance
# Class B is able to use features from class A 
# similarly class C is able to use features of class A and B 
# as class B is inheriting features from class A
class A:
    def feature1(self):
        print("This is feature 1")

class B(A):
    def feature2(self):
        print("This is feature 2")

class C(B):
    def feature3(self):
        print("This is feature 3")

a1 = A()
b1 = B()
c1 = C()


# Multiple Inheritance
# Class C is able to use features from class A and B only
class A:
    def feature1(self):
        print("This is feature 1")

class B:
    def feature2(self):
        print("This is feature 2")

class C(A,B):
    def feature3(self):
        print("This is feature 3")

a1 = A()
b1 = B()
c1 = C()
