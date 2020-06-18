
# don't forget to call function 

# function definition
def add_sub():
    x = int(input("Enter first number\n"))
    y = int(input("Enter second number\n"))

    print()    # This is used to print blank space
    
    a = x + y
    b = x - y
    c = x * y
    d = x // y
    return a,b,c,d

   

# function calling
result1,result2,result3,result4 = add_sub()   
print("Addition is",result1,"\nSubtraction is",result2,"\nMultiplication is",result3,"\nDivision is",result4)

