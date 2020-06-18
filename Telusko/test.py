# Program to display numbers from 1 to 100 
# Skipping numbers which are divisible by 3 and 5

i = 1
print("These are the numbers from 1 to 100 which are not divisible by 3 and 5 ")
for i in range(100):
    if i%3!=0 and i%5!=0:
        print(i,end=" ")    
        
