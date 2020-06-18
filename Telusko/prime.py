number = int(input("Enter Number to check\n"))
if number == 1:
    print("1 is not prime number")
else:
    for i in range(2,number):
        if number % i == 0:
            print("Number is Not Prime")
            break
    else:
        print("Number is Prime")
        