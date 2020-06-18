##############################
    #Frindship Calculator#
##############################
alphabet = 'bcghjklmpqrtvwxyz'
score = 0
names = input("Enter the first name ang give space then enter second name : -\n")
for character in names:
    if character in 'aeiou':
        score+= 5
    if character in 'friends':
        score+= 10
    if character in alphabet:
        score+=alphabet.find(character)
    else:
        score+=0

if score >75:
    print("Congratulations ! ,You both are best friends")
elif score < 100:
    print("Congratulations ! ,You both are lovers ❤ ") 
else:
    print("Your friendship score is : ",score)

