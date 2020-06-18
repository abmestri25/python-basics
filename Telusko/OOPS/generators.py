# Generator
# use yield keyword to make generators
# Generator are use to make interators in simple way

def topten():
    n = 1
    while n <= 10:
        sq = n**2
        yield sq
        n+=1


values = topten()
for i in values:
    print(i)