
# Linear Search

list = [223,332,423,5,456]

num = int(input("Enter Number to search\n"))
pos = -1
def search(list,num):
    i = 0
    while i < len(list):
        if list[i] == num:
            globals()['pos'] = i    
            return True
        i+=1
    
    return False
        

if search(list,num):
    print("Found at",pos+1)
else:
    print("Not Found")


    
