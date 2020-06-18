
def letters(names):
    greater = []
    less = []
    for i in names:
        if len(i) > 5:
            greater.append(i)
        else:
            less.append(i)  
    print("These are the names having letters greater than 5 :",greater)
    print("These are the names having letters less than 5 : ",less)  

names = []
for i in range(3):
    name = input("Enter names : ")
    names.append(name)

letters(names)