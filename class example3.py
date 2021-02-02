class Car:
    wheels = 5
    def __init__(self):
        self.color = "red"
        self.model = "bmw"


c1 = Car()
c2 = Car()
c2.color = "blue"
print(c2.__dict__)
print(c1.__dict__)
c2.wheels=4
print(c1.__dict__)
print(c2.__dict__)
print(c1.color, c2.color, c1.wheels)
print(c1.model, c2.model, c2.wheels)
