
#!/usr/bin/env python

# *** MODULES ***

# Option 1 : Import module
import greeting

# Option 2 : Import module -> specific method
#from greeting import hello

# Option 2.1 : Import module -> * method
from greeting import *

# Option 3 : Import module -> specific Class
from greeting import Greeting


if __name__ == '__main__':
    # *** Use Methods ***

    print('*** Examples Use Modules Method ***')

    greeting.hello('Hello World -> Import module')

    hello('Hello World -> Import module method')

    # *** Use Class ***

    exampleGreeting = greeting.Greeting()
    exampleGreeting.hello('Hello World -> Class')

    exampleGreeting2 = Greeting()
    exampleGreeting2.hello('Hello World 2 -> Class')
