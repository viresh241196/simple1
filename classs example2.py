class Info:
    def __init__(self, **extra):
        self.name = 'viresh'
        self.age = 23
        self.extra = extra


    def display(self):
        print(f'{self.name} has {self.age} age ')
        print(f'{self.name} compare with {c1.name} {self.extra["studies"]}')


    def display1(self):
        print(f'{self.name} has {self.age} age ')
        print(f'{self.name} compare with {c1.name} {self.extra["studies"]}')


    def compare(self, other):
        if self.age == other.age:
            print('work done')
        else:
            print('work not done')

c1 = Info(studies='Python')
c2 = Info(studies='my info')
c2.name = 'sidhu'
c2.age = 25

c1.compare(c2)

#c1.display()
#c2.display1()
#c2.display()