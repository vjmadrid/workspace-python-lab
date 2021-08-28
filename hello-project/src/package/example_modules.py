
# !/usr/bin/env python

# *** MODULES ***

# Option 1 : Import module -> specific method
from .greeting import hello, hello_message

# Option 2 : Import module -> specific Class
from .greeting import Greeting

# Option 3 : Import module -> * method and * class
# from greeting import *

if __name__ == '__main__':
    # *** Use Methods ***

    print('*** Examples Use Modules Method ***')
    hello()
    hello_message('Hello World -> Import module method')

    # *** Use Class ***

    exampleGreeting = Greeting()
    exampleGreeting.hello()
    exampleGreeting.hello_message('Hello World -> Class')
