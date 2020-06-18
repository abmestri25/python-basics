# Actual Arguments has four types 
"""
 Position
 Keyword
 Default
 Variable length
"""
#====================================#

print("Position Argument")
# you cant change the positions of arguments
def person(name,age):
    print("Name is",name)
    print("Age is",age)
    print()

person("Abhishek",21)

#=====================================#
print("Keyword Argument")
# When you dont know the sequence of argument

def person(name,age):
    print("Name is",name)
    print("Age is",age)
    print()

person(age=19,name="Saurabh")

#=======================================#
print("Default Argument")
# When any one argument is missing causes error 
# So to avoid it set default values to arguments

def person(name,age=18):
    print("Name is",name)
    print("Age is",age)
    print()

person("Shaurya")

#========================================#
print("Variable Length Argument")
# This is used when there are n number of arguments
# suppose we want to add multiple numbers
def sum(a,*b):   # *b is tuple
    c= a   
    for i in b:
        c = c + i
    print("The sum of all numbers is",c)

sum(1,2,3,4,5)

#========================================#



