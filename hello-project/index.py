# !/usr/bin/env python11
"""Top-level script to invoke helloworld implementation"""

import sys

# *** MODULES ***

# Option 1 : Import module
#from src.hello import hello
from src.hello import hello_logging

# Option 2 : Import method module
#from src.hello.hello import hello 


# import src.hello.hello
# import src.hello

# Option 3
#from src.hello import run
# Option 4
# from src.hello import run.hello

if __name__ == '__main__':
    # *** MODULES ***

    # Option 1 : Import module
    #hello.hello()
    hello_logging.hello()


    # Option 2 : Import method module
    #hello()

    #src.hello.hello()

    # Option 3 : 
    #print(run.hello())
    # sys.exit(src.hello.hello.hello())

