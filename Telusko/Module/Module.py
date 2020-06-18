def add(a,b):
    print("Addition is",a+b)

def sub(a,b):
    print("Subtraction is",a-b)

def mul(a,b):
    print("Multiplication is",a*b)

def div(a,b):
    print("Division is",a//b)


# decorator 
def smart(func):
    def wrapper(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrapper

# Connection between decorator and function
div = smart(div)
sub = smart(sub)

