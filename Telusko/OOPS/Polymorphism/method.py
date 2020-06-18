# Method Overloading
class Add:
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

s1 = Add()
print(s1.sum(23,12))

# Method Overriding


