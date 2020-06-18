
#================================#
# Anonymous Functions

square = lambda a : a**2 
print("The Square is",square(5))
#================================#
cube = lambda a : a**3 
print("The Cube is",cube(5))
#================================#
sum = lambda a,b : a+b 
print("The Sum is",sum(5,45))
#================================#
sub = lambda a,b: a-b 
print("The Subtraction is",sub(5,3))
#=========================================================#

# filter(function,iterable)

nums = [12,34,23,65,7,8,45,56,90,87,65,54,34,36]
print(nums)

evens = list(filter(lambda num : num % 2 == 0,nums))

odds = list(filter(lambda num : num % 2 == 1,nums))

print("Evens : {} and Odds : {}".format(evens,odds))

#=========================================================#
# Double the evens and odds
# map()

even_double = list(map(lambda a : a *2,evens))
odds_double = list(map(lambda a : a *2,odds))
print("Evens : {} and Odds : {}".format(even_double,odds_double))

#=========================================================#
# Add all the even doubles and odd doubles
# reduce()
from functools import reduce
even_sum = reduce(lambda a,b: a+b,even_double)
odds_sum = reduce(lambda a,b: a+b,odds_double)
print("Evens : {} and Odds : {}".format(even_sum,odds_sum))


