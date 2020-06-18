




def counter(list):
    even = 0
    odd = 0
    odds = []
    evens = []
    for i in list:        
        if i % 2 == 0:            
            evens.append(i)
            even+=1            
        else:
            odds.append(i)
            odd+=1      
    print("Even Count : {} and Odd Count : {}".format(even,odd))
    print("Even : {} and Odd : {}".format(evens,odds))


list = []
number = int(input("Enter number of elements\n"))
for i in range(number):
    number = int(input("Enter list elements : "))
    list.append(number)
print(list)

counter(list)

