
#!/usr/bin/env python

# *** MODULES ***

# Option 1 : Import module
import src.package.greeting

# Option 2 : Import module -> specific method
#from package.greeting import hello

# Option 2.1 : Import module -> * method
from src.package.greeting import *

# Option 3 : Import module -> specific Class
from src.package.greeting import Greeting


if __name__ == '__main__':
    # *** Use Methods ***

    print('*** Examples Use Modules Method ***')

    src.package.greeting.hello('Hello World -> Import module')

    hello('Hello World -> Import module method')

    # *** Use Class ***

    exampleGreeting = src.package.greeting.Greeting()
    exampleGreeting.hello('Hello World -> Class')

    exampleGreeting2 = Greeting()
    exampleGreeting2.hello('Hello World 2 -> Class')
