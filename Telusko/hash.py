# # Pattern printing

# """
# # # # # 
# # # # # 
# # # # # 
# # # # #

# """

# for i in range(4):                 
#     for j in range(4):             
#         print("#",end=" ")         
#     print()                     

# """
# # 
# # #
# # # #
# # # # #

# """
# print()
# for i in range(4):            
#     for j in range(i+1):        
#         print("#",end=" ")        
#     print()                     

# """
# # # # #
# # # # 
# # #
# #

# """

# print()
# for i in range(4):                  
#     for j in range(4-i):          
#         print("#",end=" ")      
#     print()               

# """
# 0 0 0 
# 1 1 1
# 2 2 2
# 3 3 3

# """
# print()
# for i in range(4):                
#     for j in range(4):            
#         print(i,end=" ")          
#     print()                   



# """
# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# """
# print()
# num = 1
# for i in range(4):                     
#     for j in range(i+1):         
#         print(num,end=" ")
#         num = num + 1             
#     print()   

# """
# 1  
# 2 2 
# 3 3 3 
# 4 4 4 4
# """
# print()
# num = 1
# for i in range(4):                     
#     for j in range(i+1):         
#         print(num,end=" ")
#     num = num + 1             
#     print() 

# """
# A
# A A
# A A A
# A A A A
# """
# print()
# num = 65
# for i in range(4):                     
#     for j in range(i+1): 
#         ch= chr(num)
#         print(ch,end=" ")            
#     print() 

# """
# A 
# B B
# C C C
# D D D D
# """
# print()
# num = 65
# for i in range(4):                     
#     for j in range(i+1): 
#         ch= chr(num)
#         print(ch,end=" ")
#     num = num + 1             
#     print() 

# """
# A 
# B C
# D E F
# G H I J
# """
# print()
# num = 65
# for i in range(4):                     
#     for j in range(i+1): 
#         ch= chr(num)
#         print(ch,end=" ")
#         num = num + 1             
#     print() 


"""
1 2 3 4
2 3 4
3 4
4
"""
# print()
# row = int(input("Enter number of rows\n"))
# print()
# for i in range(0,row+1,1):
#     # j=j+1
#     for j in range(i+1,row+1,1):
#         print(j,end=" ")
#     print()


"""
A P Q R
A B Q R
A B C R
A B C D

"""
print()
x = ""
word = input("Enter a string\n")
for i in word:
    x+=i
    print(x)

    
# num = 65
# for i in range(4):
#     print(chr(num))
#     for j in range(3):
#         ch= chr(num)
#         print(ch,end=" ")
        
#     print()







    