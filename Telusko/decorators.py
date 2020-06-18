# Decorators are used to add some features 
# Main function
def div(a,b):
    print("The result of division is",a/b)

# This is decorator
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

# Connecting decorator with function
# Object name should be same as function name
div = smart_div(div)
a = int(input("Enter First Number\n"))
b = int(input("Enter Second Number\n"))
div(a,b)






