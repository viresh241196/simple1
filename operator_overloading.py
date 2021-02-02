class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):                #this is used to add the functionality of adding thee to s1,s2
        n1 = self.m1 + other.m1             #and return the sum of those
        n2 = self.m2 + other.m2
        sum = {n1,n2}
        return sum

s1 = Student(50,54)
s2 = Student(55,57)

sum  = s1 + s2
print(sum)