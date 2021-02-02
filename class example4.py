class Student:
    school = "V N Sule"


    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("this is extra info")

s1 = Student(45,58,64)
s2 = Student(75,58,65)
print(s1.avg())
print(s2.avg())
#now print the school name using getschool
print(Student.getschool())  #@classmethod
print(s1.info())