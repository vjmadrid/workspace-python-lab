def hello():
    print('Hello World -> Default method')


def hello_message(msg):
    print(msg)


class Greeting():

    def __init__(self):
        pass

    def hello(self):
        print('Hello World -> Default method class')

    def hello_message(self, msg):
        print(msg)
