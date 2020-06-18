

# we can access global variable inside functions using keyword "global"
# or throughtout the code
# but we cant access local variables outside the functions or globally

a = 10    # This is global variable

def update(x):
    # Accesing global variable and reassining it to new value 
    # this is when i want to access global variable inside the function
    
    global a    #intially it was 10
    a = 20     #reassigned value of global variable a to 20
    b = 15  # this is local variable
    
    print("This is global variable a inside the function",a)   # this will print 10 
    print("This is local variable inside the function",b)  # this will print 15
 
update(a)

print("This is outside the function",a)    # this will print 20