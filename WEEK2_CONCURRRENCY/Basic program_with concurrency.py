#import threading modules
import threading

#Make the classes subclasses of 'Thread'
class Hello(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = int(num)

    def run(self):
        for i in range(self.num):
            print("Hello")

class Hi(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = int(num)


    def run(self):
        for i in range(self.num):
            print("Hi")


def main():
    num = input("Enter a number: ")

    #create objcects
    obj1 = Hello(num)
    obj2 = Hi(num)

    obj1.start()
    obj2.start()
#use member function of 'Thread' class '.start()'
#this function takes a thread from 'initialized' state to 'running' state
#when you subclass the classes that is when it has only been initilized meaning that the thtread object exists but isn't running
#using.start() tells thread to begi execution
# Ouput: RuntimeError: thread.__init__() not called
""" This is because the theading constructor should be called instead of your normal constructor:
    'def __init__(self, exec_target, exec_args):
        threading.Thread.__init__(self, target=exec_target, args=exec_args)
"""

 

main()


