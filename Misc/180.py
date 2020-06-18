# number of rows
n=5
# number of spaces 
k = 2*n - 2       #Logic

# outer loop to handle number of rows 
for i in range(0, n): 

    # inner loop to handle number spaces 

    for j in range(0, k): 
        print(end=" ") 

    # decrementing k after each loop 
    k = k - 2

    # inner loop to handle number of columns 

    for j in range(0, i+1): 
    
        # printing stars 
        print("* ", end="") 

    # ending line after each row 
    print("\r") 


'''
Output
        *
      * *
    * * *
  * * * * 
* * * * *
     
'''



