from threading import Thread
import time

class ExampleThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name=name
    
    def run(self):
        print('Started')
        
        for i in range(5):
            print('Other Thread '+str(self.name))
