import threading
import time

def example_thread_function():
    for i in range(10):
        print('Other Thread ')
        time.sleep(1)

def example_thread_function_with_parameters(name):
    for i in range(10):
        print('Other Thread '+str(name))
        time.sleep(1)

def main():
    # Create a Thread with a function without any parameters
    exampleThread = threading.Thread(target=example_thread_function)
    # Create a Thread with a function with parameters
    #exampleThread = threading.Thread(target=example_thread_function_with_parameters, args=('Name_1'))
    exampleThread.start()
    
    for i in range(10):
        print('Main Thread')
        time.sleep(1)
    
    exampleThread.join()

if __name__ == '__main__':
    main()