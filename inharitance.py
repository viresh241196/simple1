class A:
    def __init__(self):
        print("this for A init")

    def feature1(self):
        print("this is 1 feature")

    def feature2(self):
        print("this is 2 feature")

class B():
    def __init__(self):
        print("this for B init")


    def feature2(self):
        print("this is 3 feature")

    def feature4(self):
        print("this is 4 feature")


class C(B,A):
    def __init__(self):
        super().__init__()                  #it will call the init of first function specify
        print("this for c init")            #this is method resolution order


obj = C()
#ob = B()
#oa = A()
#ob.feature1()
obj.feature2()