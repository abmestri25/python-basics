
# Construct own iterator
class TopTen:
    def __init__(self):
        # counter variable
        self.num = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values = TopTen()
for i in values:
    print(i)

print()
nums = [23,34,12]
it = iter(nums)
for i in nums:
    print(it.__next__())
    
