from threading import *
from time import sleep
class Hello(Thread):                #Thread need to to inharited
    def run(self):                  #normally code run in main thread
        for i in range(5):          #run, start are some of the function inside threading
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


c1= Hello()
c2 = Hi()
c1.start()
sleep(0.2)
c2.start()
c1.join()                       #this tell main to let c1 join
c2.join()
print("Bye")