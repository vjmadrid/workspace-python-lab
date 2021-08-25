import time

from src.hello.hello_thread_class import ExampleThread

def main():
    exampleThread = ExampleThread('Name_1')
    exampleThread.start()

    for i in range(5):
        print('Main Thread')
        time.sleep(1)

    exampleThread.join()

if __name__ == '__main__':
    main()