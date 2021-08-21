
#!/usr/bin/env python11

"""Top-level script to invoke helloworld implementation"""

import sys
import src.hello.hello
#import src.hello
# Option 1
from src.hello import run
# Option 2
from src.hello import run.hello

if __name__ == '__main__':
    # Option 1
    print(run.hello())
    #sys.exit(src.hello.hello.hello())