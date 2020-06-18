# globals()[''] is used when we want to use both
# local as well as global variable with same variable
# in below code "a" is that variable

a = 10   # Initial Global Variable

def something():
    a = 9
  
    print("Local variable 'a' inside function :",a)
    globals()['a'] = 15    # Reassigned value
    
something()

print("This is global varibale a :",a)   