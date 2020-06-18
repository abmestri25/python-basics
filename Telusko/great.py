# Program to find smallest and largest number from the list
# this is the empty list to store numbers
# initially it has to be blank or empty
num = []
# for loop is to get input for the list
for i in range(3):
    print("Enter", i+1,"st number")
    numbers = int(input())
    # append() function to add numbers to list
    num.append(numbers)

print("List Elements are as follows ;")
for i in num:
    print(i,end=" ")

print("\n")
print(max(num),"is the largest number from the list")
print(min(num),"is the smallest number from the list")