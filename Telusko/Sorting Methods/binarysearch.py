
# list should be sorted to apply binary search

'''
        5 , 12, 23, 32, 44, 45, 64, 323
        ^                            ^
    lower bound                  upper bound

    mid = (lower bound + upper bound) // 2   .... which returns mid element
'''

pos = -1
def search(list,n):
    l = 0    
    u = len(list)-1
    while l <= u:
        mid = (l+u) // 2
        if list[mid]==n:
            globals()['pos']= mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1            
    return False

list = [12,323,23,45,44,5,64,32]
list.sort()   #-->  Sorted list  5, 12, 23, 32, 44, 45, 64, 323
print(list)

n = int(input("Enter number to search \n"))
if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")
