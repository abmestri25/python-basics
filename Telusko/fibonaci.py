

#  Output :
#  0 1 1 2 3 5 8 13 21 .....

def series():
    number = int(input("Enter Number\n"))    
    first = 0
    second = 1
    list = []
    if number < 0 :
        print("Invalid Number")
    else:
        if number == 1:
            print(first,end=" ")
        else:
            # print(first,end=" ")
            # print(second,end=" ")
            for i in range(2,number):
                # This is the logic for the next numbers
                next = first + second
                first = second
                second = next
                list.append(next)
                  
                print(list[-1])
                           
series()


# a = 0
# b = 1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(2,5):
#     c = a + b
#     a = b
#     b  = c
#     print(c,end=" ")