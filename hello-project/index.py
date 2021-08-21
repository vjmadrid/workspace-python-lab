
#!/usr/bin/env python11

"""Top-level script to invoke helloworld implementation"""

import sys

# *** MODULES ***

# Option 1 : Import module
import greeting

# Option 2 : Import module -> method
#from greeting import greeting

#import src.hello.hello
#import src.hello
# Option 2
#from src.hello import run
# Option 3
#from src.hello import run.hello

if __name__ == '__main__':
    # *** MODULES ***

    # Option 1 : Import module
    greeting.hello()

    # Option 2 : Import module -> method
    #greeting()

    #src.hello.hello.hello()
    
    # Option 1
    #print(run.hello())
    #sys.exit(src.hello.hello.hello())