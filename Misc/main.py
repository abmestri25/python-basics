# name = "Abhi,Sanjay,Mestri"
# result= name.split(",")
# print(result)

# text = "Hey! No worries. She said that I'll be coming there"
# print(text)


# Array #for_LOOp
Movies = ["3 idiots","Geetha Govindam","Good News"]  #array
num=1
for i in Movies:
    print(num, i)
    num = num + 1


print("I like",Movies[0])


# Dictionary
Dict = {"Name":"Abhi","Age":20,"Year":"Third"} # Dictionary
print(Dict)
# Using For Loop
for key , value in Dict.items():
    print(key,":",value)

# Variables
print(len(Dict))

# num = [45,2,4,6,8,11,22,36,1]
# alphabets = ["Q","W","E","R","T"]
# print(sorted([45,2,4,6,8,11,22,36,1]))
# print(sorted(num))
# print(sorted(alphabets))


# Function

def print_name(Name="Someone",Age="Unknown"):
    print("My name is",Name,"and My age is",Age)


print_name("Abhishek",21)


def print_people(*people):
    for person in people:
        print("The person is",person)



print_people("Abhi","Saurabh","Prem","Sanjay","Prakash","Milind","Shaurya")
