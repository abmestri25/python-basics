
# Factorial using Recursion including user input
#=================================================#
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
        
num = int(input("Enter number\n"))
result = fact(num)
print("The Factorial of",num,"is",result)


# Factorial using function
#=================================================#
def fact(n):
    f = 1
    for i in range(2,n+1):
        f = f * i
    print("Factorial of", n, "is",f)

fact(4)



        
   

