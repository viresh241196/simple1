class Person:
    def __init__(self, name, **thank):
        self.name = name
        self.thank = thank


    def talk1(self):
        print(f"hi there {self.name}")
        print(f'this is {self.thank["bye"]}')

    def talk2(self):
        print(f"hi there {self.name}")


object = Person("viresh", bye='thank you')
object.talk1()
print(object.thank['bye'])
object1 = Person("sidhu")
object1.talk2()

