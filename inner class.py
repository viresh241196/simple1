class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop('hp', 6)

    def show(self):
        print(f'{self.name} has roll number = {self.rollno}')


    def getname(self):
        return print(self.name)


    class Laptop:
        def __init__(self, model, ram):
            self.model = model
            self.ram =ram


        def show(self):
            print(f' has a {self.model} model laptop with {self.ram}GB ram')


s1 = Student('viresh', 24)
s2 = Student('sidhu', 26)
s1.getname()
#s1.lap = Student.Laptop("sony", 6)
s1.lap.model = "sony"
s1.lap.ram = 8
print(s1.lap.show())
s2.getname()
print(s2.lap.show())