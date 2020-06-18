# for else 
# "break" keyword is mandatory 

nums = [23,34,46,12,54]

for num in nums:
    if num % 5 == 0:
        print(num,"is divisible by 5")
        break
else:
    print("Number not found")
