
# Selection Sort

def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if list[j] < list[minpos]:
                minpos = j
                
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
        
    return list

list = [12,323,23,45,22,55,78]
print("Unsorted List : ",list)
print("Sorted List : ",sort(list))  
