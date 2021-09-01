
# !/usr/bin/env python

# *** MODULES ***

# Option 1 : Import module
# import src.package.greeting

# Option 2 : Import module -> specific method
from src.package.greeting import hello, hello_message

# Option 2.1 : Import module -> * method
# from src.package.greeting import *
from src.package import greeting

# Option 3 : Import module -> specific Class
from src.package.greeting import Greeting

if __name__ == '__main__':
    # *** Use Methods ***

    print('*** Examples Use Modules Methods ***')
    hello()
    hello_message('Hello World -> Import module')

    print('*** Examples Use File Methods ***')
    greeting.hello()
    greeting.hello_message('Hello World -> Import module')

    # *** Use Class ***

    exampleGreeting = greeting.Greeting()
    exampleGreeting.hello()
    exampleGreeting.hello_message('Hello World -> Class')

    exampleGreeting2 = Greeting()
    exampleGreeting2.hello()
    exampleGreeting2.hello_message('Hello World 2 -> Class')
