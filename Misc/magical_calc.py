import re  #regular expression in-built library
print("####   MAGICAL CALCULATOR   ####")
print("Enter 1 For Calculation")
print("Type 'quit' to exit")

run = True
while run:
    
    choice = input("Enter Your Choice \n")
    if choice == '1':
        eqa = input("Enter Equation\n")
        equation =re.sub('[a-zA-Z,.:=()" "]','',eqa)
        print("Result is",eval(equation))
    elif choice == 'quit':
        run = False
    else:
        print("Wrong Choice")


