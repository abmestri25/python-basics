# Bubble Sort



def sort(list):
    for i in range(len(list)-1,0,-1):
        
        for j in range(i):
            # if first number is greater than second number
            # swap
            if list[j] > list[j+1]:
                temp = list[j]
                list[j]= list[j+1]
                list[j+1]= temp
    return list


list = [12,323,23,45,44,5,64,32]

print("Unsorted List : ",list)
print("Sorted List : ",sort(list))

