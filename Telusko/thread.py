from threading import *
from time import sleep

# Two different threads t1 and t2 
# there is main thread which is responsible to print "Bye..."

# t1 Thread
class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)


# t2 Thread
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
            
# Objects
t1 = Hii()
t2 = Hello()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye.....")
