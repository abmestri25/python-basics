try:
    print("File is opened.")
    a = int(input("Enter a number\n"))
    b = int(input("Enter a number\n"))
    print(a//b)

except Exception as e:
    print("Something went wrong.. ",e)

finally:
    print("File is closed.")